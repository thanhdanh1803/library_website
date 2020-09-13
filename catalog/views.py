from django.shortcuts import render
from cart.forms import *
from catalog.models import *
from cart.cart import Cart

# Create your views here.
def home(request):
    book_list = Book.objects.order_by('title')
    cart = Cart(request)
    context_dict = {'books': book_list, 'cart':cart}
    return render(request, 'catalog/home.html', context=context_dict)

def book_detail(request, id = None):
    book = Book.objects.get(pk= id)
    books_instance = BookInstance.objects.order_by('id')
    book_instance = []
    for b in books_instance:
        if b.book == book:
            book_instance.append(b)
    cart_book_form = BookOrderForm()
    return render(request, 'catalog/bookdetail.html', context={"book": book, "books_instance": book_instance, 'cart_form': cart_book_form})

    
    