from django.conf import settings
from catalog.models import Book, BookInstance
from datetime import datetime

class Cart(object):
    '''
    classdocs:
    '''
    def __init__(self, request):
        '''
        initialize the session
        '''
        print('Session init')
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def add(self, book_instance, due_date):
        book_id = str(book_instance.id)
        self.cart[book_id] = {'start_day': datetime.strftime(datetime.now(), '%d/%m/%Y %H:%M:%S'), 'due_date':datetime.strftime(due_date, '%d/%m/%Y')}
        self.save()
    def add_user(self, username, password):
        self.username = username
        self.password = password
    def remove(self, book_instance):
        book_id = str(book_instance.pk)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()
    def clear(self):
        self.cart = {}
        self.session[settings.CART_SESSION_ID] = {}
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    
    def __iter__(self):
        book_ids = self.cart.keys()
        book_instances = BookInstance.objects.filter(id__in = book_ids)
        for book in book_instances:
            self.cart[str(book.pk)]['book_instance'] = book
        for item in self.cart.values():
            yield item
    
    def __len__(self):
        """
        count all items in the cart
        """
        return len(self.cart)