from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import json

from shop.models import Product
# from shop.views import get_products
from .cart import Cart


def find_product_by_id(id):
    return Product.objects.get(pk=id)


# from shop.views import get_products
@login_required(login_url="log_in")
def cart_add(request, id):
    cart = Cart(request)
    product = find_product_by_id(id)
    cart.add(product=product)
    get_total_amount = cart.get_total_amount()
    request.session['total_amount_in_cart_products'] = json.dumps(float(get_total_amount))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url="log_in")
def item_clear(request, id):
    cart = Cart(request)
    product = find_product_by_id(id)
    cart.remove(product)
    get_total_amount = cart.get_total_amount()
    request.session['total_amount_in_cart_products'] = json.dumps(float(get_total_amount))
    return redirect("cart_detail")


@login_required(login_url="log_in")
def item_increment(request, id):
    cart = Cart(request)
    product = find_product_by_id(id)
    cart.add(product=product)
    get_total_amount = cart.get_total_amount()
    request.session['total_amount_in_cart_products'] = json.dumps(float(get_total_amount))
    return redirect("cart_detail")


@login_required(login_url="log_in")
def item_decrement(request, id):
    cart = Cart(request)
    product = find_product_by_id(id)
    cart.substract(product=product)
    get_total_amount = cart.get_total_amount()
    request.session['total_amount_in_cart_products'] = json.dumps(float(get_total_amount))
    return redirect("cart_detail")


@login_required(login_url="log_in")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    get_total_amount = cart.get_total_amount()
    request.session['total_amount_in_cart_products'] = json.dumps(float(get_total_amount))
    return redirect("cart_detail")

def sum_to_pay(request):
    cart = Cart(request)
    return len(cart)

@login_required(login_url="log_in")
def cart_detail(request):
    if request.method == 'POST':
        selected_lang = request.POST.get('selected_lang', '0')
        request.session['lang'] = selected_lang

    selected_lang = request.session.get('lang')
    if not selected_lang:
        selected_lang = 'geo'
    cart = Cart(request)
    # total_price = cart.total_price()

    get_total_price = cart.get_total_price()
    request.session['total_price_in_cart_products'] = json.dumps(float(get_total_price))

    get_total_weight = cart.get_total_weight()
    request.session['total_weight_in_cart_products'] = json.dumps(float(get_total_weight))

    get_total_amount = cart.get_total_amount()
    request.session['total_amount_in_cart_products'] = json.dumps(float(get_total_amount))

    params = {'get_total_price': get_total_price, 'selected_lang': selected_lang}
    return render(request, 'shop/cart.html', params)

# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from shop.models import Product
# from .cart import Cart
# from .forms import CartAddProductForm
#
# @login_required(login_url="log_in")
# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
#     return redirect('cart_detail')
#
# @login_required(login_url="log_in")
# def cart_remove(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     cart.remove(product)
#     return redirect('cart_detail')
#
# @login_required(login_url="log_in")
# def cart_detail(request):
#     cart = Cart(request)
#     return render(request, 'shop/cart.html', {'cart': cart})