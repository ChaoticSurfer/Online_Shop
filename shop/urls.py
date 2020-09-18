from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('products/', views.products, name="Products"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('tracker/', views.tracker, name="TrackingStatus"),
    path('search/', views.search, name="Search"),
    path('productView/<int:my_product_id>', views.productView, name="ProductView"),
    path('checkout/', views.checkout, name="Checkout"),
    # path('cart/', views.cart, name="Cart"),
    path('checkout/', views.checkout, name="Checkout"),
    # path('register', views.registration, name="Registration")

    # path('products/filter=?<filter_product>/sort=?<order_by>/'),
    # path('products/filter=?<filter_product>/'),
    # path('products/sort=?<order_by>/'),
    path('products/sort=<order>/filter=<filter_product>/', views.products_sorted_filter),
    path('products/filter=<filter_product>/sort=<order>/', views.products_filter_sorted),
    path('products/filter=<filter_product>/', views.products_filter, name="Filter"),
    path('products/sort=<order>/', views.products_sorted, name="Order"),
    path('404/not_found/', views.redirect, name="Redirect"),
    path('delivery/', views.delivery, name="Delivery"),
    path('checkout/', views.checkout, name="Checkout")
]
