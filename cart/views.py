from django.shortcuts import render
from django.views.decorators.http import require_POST
from catalog.models import Book, BookInstance
from .cart import Cart
from .forms import BookOrderForm
from django.shortcuts import *
# Create your views here.

@require_POST
def cart_add(request, book_id = None):
    cart = Cart(request)
    book = get_object_or_404(BookInstance, id = book_id)
    form = BookOrderForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(book_instance=book, weeks =cd['duration'])
    return redirect('cart:cart_detail')
def cart_remove(request, book_id = None):
    cart = Cart(request)
    book = get_object_or_404(BookInstance, id = book_id)
    cart.remove(book)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = BookOrderForm(initial={'duration':item['duration'], 'update': True})
        print(item.keys())
    return render(request, 'cart/cart_detail.html', {'cart':cart})

# def cart_update(require, book_id = None):
#     cart = Cart(render)
#     book = get_object_or_404(BookInstance, id = book_id)
#     cart.cart_update(cart)
#     return redirect('cart:cart_detail')