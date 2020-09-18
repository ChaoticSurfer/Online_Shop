from django.contrib.auth.decorators import login_required
from datetime import datetime as django_datetime
from datetime import timedelta
from itertools import chain
#ჩავამატე
# from django.http import JsonResponse
import json
from authentication.models import *
# from .utils import cookieCart, cartData

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
import pathlib
from cart import *
#ესეც ჩავამატე
# from authentication.models import User, Order

from .models import Brand, Product, Paint_Oil_Color_Product, Paint_Acrylic_Color_Product, \
    Paint_Gouache_Color_Product, Paint_Water_Color_Product, Paint_Other_Color_Product, Pastel_Oil_Color_Product, \
    Pastel_Soft_Color_Product, Pastel_Water_Color_Product, \
    Pastel_Dry_Color_Product, Pencil, Accessories_Molbert, Accessories_Auxiliary_Fluids, Accessories_Palette, \
    Accessories_Mastehin, Canvas_rectangle_frame, Canvas_circular_frame, \
    Canvas_with_rectangle_frame, Canvas_with_circular_frame, Drawing_canvas, Tree_drawing_board, Water_color_sheet, \
    Canvas_with_carton

from django import template

# def view_404(requests, exception):
#     return render(requests, 'shop/404.html')



def redirect(request):
    selected_lang = request.session.get('lang')
    if not selected_lang:
        selected_lang = 'geo'

    params = {'selected_lang': selected_lang}
    return render(request,'shop/404.html', params)




# Create your views here.
def index(request):
    if request.method == 'POST':
        selected_lang = request.POST.get('selected_lang', '0')
        request.session['lang'] = selected_lang

    selected_lang = request.session.get('lang')
    if not selected_lang:
        selected_lang = 'geo'
    # data = cartData(request)
    #
    # cartItems = data['cartItems']
    # order = data['order']
    # items = data['items']

    brands = Brand.objects.all()
    paginator = Paginator(brands, 20)
    page = request.GET.get('page')
    brands = paginator.get_page(page)
    params = {'brands': brands, 'selected_lang': selected_lang}
    # 'cartItems':cartItems}
    return render(request, 'shop/main.html', params)


def products(request):
    if request.method != 'POST':
        selected_lang = request.session.get('lang')
    if request.method == 'POST':
        selected_lang = request.POST.get('selected_lang', '0')
        request.session['lang'] = selected_lang

    selected_lang = request.session.get('lang')
    if not selected_lang:
        selected_lang = 'geo'



    # data = cartData(request)
    #
    # cartItems = data['cartItems']
    # cart_order = data['order']
    # items = data['items']
    # current_date = django_datetime.now()
    today = django_datetime.now() - timedelta(days=1)
    paginator = Paginator(get_products(), 30)
    page = request.GET.get('page')
    a = paginator.get_page(page)




    params = {'a': a, 'today': today, 'selected_lang': selected_lang}

    # 'cartItems':cartItems}
    return render(request, 'shop/products.html', params)


def products_sorted_filter(request, order, filter_product):
    if request.method == 'POST':
        selected_lang = request.POST.get('selected_lang', '0')
        request.session['lang'] = selected_lang

    selected_lang = request.session.get('lang')
    if not selected_lang:
        selected_lang = 'geo'
    p = get_products()
    # if filter_product != 'none':
    #     p = [i for i in p if filter_product in i.verbose_name]
    if order == 'asc':
        p.sort(key=lambda x: x.price, reverse=False)
        p = [i for i in p if str(filter_product) in i.verbose_name or str(filter_product) in i.sub_verbose_name]
    elif order == 'desc':
        p.sort(key=lambda x: x.price, reverse=True)
        p = [i for i in p if str(filter_product) in i.verbose_name or str(filter_product) in i.sub_verbose_name]
    else:
        return HttpResponse("wrong")


    today = django_datetime.now() - timedelta(days=1)
    paginator = Paginator(p, 30)
    page = request.GET.get('page')
    a = paginator.get_page(page)
    params = {'a': a, 'today': today, 'selected_lang': selected_lang}
    return render(request, 'shop/products.html', params)


def products_filter_sorted(request, filter_product, order):
    if request.method == 'POST':
        selected_lang = request.POST.get('selected_lang', '0')
        request.session['lang'] = selected_lang

    selected_lang = request.session.get('lang')
    if not selected_lang:
        selected_lang = 'geo'
    # data = cartData(request)
    #
    # cartItems = data['cartItems']
    # cart_order = data['order']
    # items = data['items']

    p = get_products()
    if filter_product != 'none':
        p = [i for i in p if str(filter_product) in i.verbose_name or str(filter_product) in i.sub_verbose_name]
    if order == 'asc':
        p.sort(key=lambda x: x.price, reverse=False)
    elif order == 'desc':
        p.sort(key=lambda x: x.price, reverse=True)
    else:
        return HttpResponse("wrong")
        # return redirect(redirect(request))



    # current_date = django_datetime.now()
    today = django_datetime.now() - timedelta(days=1)
    paginator = Paginator(p, 30)
    page = request.GET.get('page')
    a = paginator.get_page(page)
    params = {'a': a, 'today': today, 'selected_lang': selected_lang}
              # 'cartItems':cartItems}
    return render(request, 'shop/products.html', params)


def products_filter(request, filter_product):
    if request.method == 'POST':
        selected_lang = request.POST.get('selected_lang', '0')
        request.session['lang'] = selected_lang

    selected_lang = request.session.get('lang')
    if not selected_lang:
        selected_lang = 'geo'
    # data = cartData(request)
    #
    # cartItems = data['cartItems']
    # cart_order = data['order']
    # items = data['items']

    p = get_products()
    p = [i for i in p if str(filter_product) in i.verbose_name or str(filter_product) in i.sub_verbose_name]

    # current_date = django_datetime.now()
    today = django_datetime.now() - timedelta(days=1)
    paginator = Paginator(p, 30)
    page = request.GET.get('page')
    a = paginator.get_page(page)
    params = {'a': a, 'today': today, 'selected_lang': selected_lang}
    # 'cartItems':cartItems}
    return render(request, 'shop/products.html', params)


def products_sorted(request, order):
    if request.method == 'POST':
        selected_lang = request.POST.get('selected_lang', '0')
        request.session['lang'] = selected_lang

    selected_lang = request.session.get('lang')
    if not selected_lang:
        selected_lang = 'geo'
    # data = cartData(request)
    #
    # cartItems = data['cartItems']
    # cart_order = data['order']
    # items = data['items']

    p = get_products()
    # order = request.GET.get('order')
    # order = request.GET.get('sort')
    if order == 'asc':
        p.sort(key=lambda x: x.price, reverse=False)
    elif order == 'desc':
        p.sort(key=lambda x: x.price, reverse=True)
    else:
        return HttpResponse('wrong')
        # return redirect(redirect(request))

    today = django_datetime.now() - timedelta(days=1)
    paginator = Paginator(p, 30)
    page = request.GET.get('page')
    a = paginator.get_page(page)
    params = {'a': a, 'today': today, 'selected_lang': selected_lang}
    # 'cartItems':cartItems}
    return render(request, 'shop/products.html', params)


def about(request):
    if request.method == 'POST':
        selected_lang = request.POST.get('selected_lang', '0')
        request.session['lang'] = selected_lang

    selected_lang = request.session.get('lang')
    if not selected_lang:
        selected_lang = 'geo'
    # data = cartData(request)
    #
    # cartItems = data['cartItems']
    # cart_order = data['order']
    # items = data['items']
    params = {'selected_lang': selected_lang}
    # 'cartItems':cartItems}
    return render(request, 'shop/aboutUs.html', params)


def contact(request):
    if request.method == 'POST':
        selected_lang = request.POST.get('selected_lang', '0')
        request.session['lang'] = selected_lang

    selected_lang = request.session.get('lang')
    if not selected_lang:
        selected_lang = 'geo'
    # data = cartData(request)
    #
    # cartItems = data['cartItems']
    # cart_order = data['order']
    # items = data['items']
    params = {'selected_lang': selected_lang}
    # 'cartItems': cartItems}
    return render(request, 'shop/contact.html', params)


def tracker(request):
    return HttpResponse("tracker")


def search(request):
    return HttpResponse("search")


def productView(request, my_product_id):
    if request.method == 'POST':
        selected_lang = request.POST.get('selected_lang', '0')
        request.session['lang'] = selected_lang

    selected_lang = request.session.get('lang')
    if not selected_lang:
        selected_lang = 'geo'
    # data = cartData(request)
    #
    # cartItems = data['cartItems']
    # cart_order = data['order']
    # items = data['items']

    product = Product.objects.filter(id=my_product_id)
    return render(request, 'shop/productView.html', {'product': product[0], 'a': get_products(), 'selected_lang': selected_lang})
    # 'cartItems':cartItems})


def checkout(request):
    if request.method == 'POST':
        selected_lang = request.POST.get('selected_lang', '0')
        request.session['lang'] = selected_lang

    selected_lang = request.session.get('lang')
    if not selected_lang:
        selected_lang = 'geo'

    exact_area = request.session.get('exact_area')
    phone_number = request.session.get('phone_number')




    params = {'selected_lang': selected_lang, 'exact_area':exact_area, 'phone_number':phone_number}
    return render(request, 'shop/checkout.html', params)

# def cart(request):
#     # data = cartData(request)
#     #
#     # cartItems = data['cartItems']
#     # cart_order = data['order']
#     # items = data['items']
#
#     params = {}
#     # 'items': items, 'cart_order': cart_order, 'cartItems': cartItems}
#     return render(request, 'shop/cart.html', params)

def get_products():
    paints1 = Paint_Oil_Color_Product.objects.all()
    paints2 = Paint_Acrylic_Color_Product.objects.all()
    paints3 = Paint_Gouache_Color_Product.objects.all()
    paints4 = Paint_Water_Color_Product.objects.all()
    paints5 = Paint_Other_Color_Product.objects.all()
    pastels1 = Pastel_Oil_Color_Product.objects.all()
    pastels2 = Pastel_Soft_Color_Product.objects.all()
    pastels3 = Pastel_Water_Color_Product.objects.all()
    pastels4 = Pastel_Dry_Color_Product.objects.all()
    pencils = Pencil.objects.all()
    accessories1 = Accessories_Molbert.objects.all()
    accessories2 = Accessories_Auxiliary_Fluids.objects.all()
    accessories3 = Accessories_Palette.objects.all()
    accessories4 = Accessories_Mastehin.objects.all()
    # drawing_boards = Drawing_boards.objects.all()
    canvas_rectangle_frame = Canvas_rectangle_frame.objects.all()
    canvas_circular_frame = Canvas_circular_frame.objects.all()
    canvas_with_rectangle_frame = Canvas_with_rectangle_frame.objects.all()
    canvas_with_circular_frame = Canvas_with_circular_frame.objects.all()
    # drawing_canvas = Drawing_canvas.objects.all()
    tree_drawing_board = Tree_drawing_board.objects.all()
    water_color_sheet = Water_color_sheet.objects.all()
    canvas_with_carton = Canvas_with_carton.objects.all()
    a = list(
        chain(paints1, paints2, paints3, paints4, paints5, pastels1, pastels2, pastels3, pastels4, pencils,
              accessories1,
              accessories2, accessories3, accessories4, canvas_rectangle_frame, canvas_circular_frame,
              canvas_with_rectangle_frame,
              canvas_with_circular_frame, tree_drawing_board, water_color_sheet, canvas_with_carton))
    return a

def error_404(request, exception):
    if request.method == 'POST':
        selected_lang = request.POST.get('selected_lang', '0')
        request.session['lang'] = selected_lang

    selected_lang = request.session.get('lang')
    if not selected_lang:
        selected_lang = 'geo'
    data = {'selected_lang': selected_lang}
    return render(request, 'shop/404.html', data)

@login_required(login_url="log_in")
def delivery(request):
    if request.method == 'POST':
        selected_lang = request.POST.get('selected_lang', '0')
        request.session['lang'] = selected_lang

    selected_lang = request.session.get('lang')
    if not selected_lang:
        selected_lang = 'geo'



    if request.method == 'POST':
        selected_area = request.POST.get('selected_area', '0')
        request.session['area'] = selected_area

    selected_area = request.session.get('area')
    if not selected_area:
        selected_area = ''


    total_price_in_cart_products = request.session.get('total_price_in_cart_products')
    if total_price_in_cart_products == None:
        total_price_in_cart_products = 0


    total_weight_in_cart_products = request.session.get('total_weight_in_cart_products')
    if total_weight_in_cart_products == None:
        total_weight_in_cart_products = 0


    if selected_area == 'თბილისი' and float(total_price_in_cart_products) >= 50:
        tax = 5
        request.session['delivery_method'] = ('True')
        request.session['tax'] = float(tax)
    elif selected_area == 'თბილისი' and float(total_price_in_cart_products) < 50 and float(total_price_in_cart_products) != 0:
        tax = 10
        request.session['delivery_method'] = ('True')
        request.session['tax'] = float(tax)
    elif selected_area == 'თბილისი' and float(total_price_in_cart_products) == 0:
        tax = 0
        request.session['delivery_method'] = ('True')
        request.session['tax'] = float(tax)
    elif selected_area != 'აბაშიძის ფილიალი' and selected_area != 'გახოკიძის ფილიალი' and selected_area != 'კოსტავას ფილიალი' and selected_area != 'რუსთაველის ფილიალი' and selected_area != 'ჯორჯაძის ფილიალი' and selected_area != 'თბილისი':
        tax = (float(total_weight_in_cart_products)//1)*10
        request.session['delivery_method'] = ('True')
        request.session['tax'] = float(tax)
    elif selected_area == 'აბაშიძის ფილიალი' and selected_area == 'გახოკიძის ფილიალი' and selected_area == 'კოსტავას ფილიალი' and selected_area == 'რუსთაველის ფილიალი' and selected_area == 'ჯორჯაძის ფილიალი':
        tax = 0
        request.session['delivery_method'] = ('False')
        request.session['tax'] = float(tax)
    else:
        tax = 0
        request.session['delivery_method'] = ('False')
        request.session['tax'] = float(tax)



    if request.method == 'POST':
        exact_area = request.POST.get('exact_area', '0')
        phone_number = request.POST.get('phone_number', '0')
        request.session['exact_area'] = exact_area
        request.session['phone_number'] = phone_number

    exact_area = request.session.get('exact_area')
    phone_number = request.session.get('phone_number')
    if not exact_area:
        exact_area = ''
    elif not phone_number:
        phone_number = ''

    params = {'selected_lang': selected_lang, 'selected_area': selected_area, 'tax':tax}

    return render(request, 'shop/delivery.html', params)

# def language(request):
#     request.session['lang'] = 'eng'






# def error_500(request, exception):
#     data = {}
#     return render(request, 'certman/500.html', data)