from django.db import models
from django.db.models import DO_NOTHING
from authentication.models import User
from django.utils import timezone
from shop.models import Product
from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator, MaxValueValidator, \
    EmailValidator
from datetime import datetime as django_datetime
import datetime
from django.forms import ModelForm
from django.db.models import Sum


# class Successful_Transaction(models.Model):
#     transaction_id = models.AutoField
#     transaction_time = models.DateTimeField
#     user = models.ForeignKey(User, on_delete=DO_NOTHING)
#     price_paid = models.FloatField
#     place_to_be_delivered = models.IntegerField


class SuccessfulTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=DO_NOTHING)
    order_code = models.CharField(max_length=5, editable=False, default=0)
    transaction_id = models.AutoField(primary_key=True, default=0)
    transaction_time = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(blank=True, max_length=20)
    delivery = models.BooleanField(default=False)
    address = models.CharField(blank=True, max_length=150)
    total_price = models.FloatField()
    ip = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return self.transaction_time

    def __unicode__(self):
        return self.transaction_id

    # @property
    # def revenue(self):
    #     return self.total_price*0.8

class OrderForm(ModelForm):
    class Meta:
        model = SuccessfulTransaction
        fields = ['user', 'delivery', 'address', 'phone', 'total_price']


class OrderProduct(models.Model):
    order = models.ForeignKey(SuccessfulTransaction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    price = models.FloatField()
    total_price = models.FloatField()
    order_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name, self.product.product_name_geo, self.product.product_id, self.price, self.quantity, self.total_price, self.order_time

