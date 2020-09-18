from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .forms import CreateUserForm
# from django.http import JsonResponse
# import json
from authentication.models import *
# from shop.utils import cookieCart, cartData
# from authentication.models import User, Order


def registreration(request):
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


    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            login(request, user)
            first_name = form.cleaned_data.get('first_name')
            '''Success needs to be implemented In next page'''
            if first_name:
                messages.info(request, f'Account Was Created for {first_name} And Logged in')
            else:
                messages.info(request, f'Account Was Created for {form.cleaned_data.get("email")} And Logged in')
            '''end of success message'''
            return redirect('ShopHome')
        # else:
        #     messages.info(request, "Input Proper Data")
        elif selected_lang is not None and form.is_valid() == True:
            return redirect(HttpResponseRedirect)
        elif selected_lang == '0' and form.is_valid() == False:
            messages.info(request, "Input Proper Data")
    params = {'form': form, 'selected_lang': selected_lang}
              # 'cartItems':cartItems}
    return render(request, 'registration.html', params)


'''request.user for login info in template'''


def log_in(request):
    if request.method == 'POST':
        selected_lang = request.POST.get('selected_lang', '0')
        request.session['lang'] = selected_lang

    selected_lang = request.session.get('lang')
    if not selected_lang:
        selected_lang = 'geo'
    # data = cartData(request)

    # cartItems = data['cartItems']
    # order = data['order']
    # items = data['items']


    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('ShopHome')
        elif selected_lang is not None and user is not None:
            selected_lang = request.session.get('lang')
            return redirect(HttpResponseRedirect)
        elif selected_lang == '0' and user is None:
            selected_lang = request.session.get('lang')
            messages.info(request, "Email or Password Is  Incorrect")
        # else:
        #     messages.info(request, "Email or Password Is  Incorrect")
    params = {'selected_lang': selected_lang}
    return render(request, 'login.html', params)


def log_out(request):
    logout(request)
    return redirect('log_in')



# Create your views here.