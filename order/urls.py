from django.urls import path
from . import views


urlpatterns = [
    # path("income/", views.incomeForADmin, name="income"),
    path('orderproduct/', views.orderproduct, name='orderproduct')
]