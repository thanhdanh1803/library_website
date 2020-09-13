from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate
from catalog.models import Book, BookInstance
from .cart import Cart
from registration.user_session import UserSession
from .forms import BookOrderForm
from django.shortcuts import *
from datetime import datetime

# Create your views here.

@require_POST
def cart_add(request, book_id = None):
    cart = Cart(request)
    book = get_object_or_404(BookInstance, id = book_id)
    form = BookOrderForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        print('date:',cd['due_date'])
        cart.add(book_instance=book, due_date =cd['due_date'])
    return redirect('cart:cart_detail')
def cart_remove(request, book_id = None):
    cart = Cart(request)
    book = get_object_or_404(BookInstance, id = book_id)
    cart.remove(book)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = BookOrderForm(initial={'due_date':item['due_date'], 'update': True})
    return render(request, 'cart/cart_detail.html', {'cart':cart})

@require_POST
def cart_submit(request):
    cart = Cart(request)
    username = request.session['username']
    password = request.session['password']
    user = authenticate(username=username, password=password )
    for item in cart:
        book_id = item['book_instance'].id
        book_instance = BookInstance.objects.get(pk = book_id)
        book_instance.status = 'o'
        book_instance.due_back= datetime.strptime(item['due_date'], '%d/%m/%Y') 
        book_instance.borrower = user
        print(book_instance)
        print(book_instance.due_back)
        print(book_instance.status) 
        book_instance.save()
    cart.clear()
    result = "Đặt hàng thành công"
    return render(request, "catalog/home.html", {"result":result})

# def cart_update(require, book_id = None):
#     cart = Cart(render)
#     book = get_object_or_404(BookInstance, id = book_id)
#     cart.cart_update(cart)
#     return redirect('cart:cart_detail')