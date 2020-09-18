from django.db import models
# from django.db import models
# from django.db.models import DO_NOTHING
# from authentication.models import User
# from django.utils import timezone
# from shop.models import Product
# from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator, MaxValueValidator, \
#     EmailValidator
# from datetime import datetime as django_datetime
# import datetime
# from django.forms import ModelForm
#
# # class Successful_Transaction(models.Model):
# #     transaction_id = models.AutoField
# #     transaction_time = models.DateTimeField
# #     user = models.ForeignKey(User, on_delete=DO_NOTHING)
# #     price_paid = models.FloatField
# #     place_to_be_delivered = models.IntegerField
#
#
# class Successful_Transaction(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
#     transaction_id = models.AutoField
#     transaction_time = models.DateTimeField(auto_now_add=True)
#     phone = models.CharField(blank=True, max_length=20)
#     delivery_type = models.BooleanField(default=False)
#     address = models.CharField(blank=True, max_length=150)
#     total_price = models.FloatField()
#     ip = models.CharField(blank=True, max_length=20)
#
#     def __str__(self):
#         return self.user.name, self.user.email
#
# class OrderForm(ModelForm):
#     class Meta:
#         model = Successful_Transaction
#         fields = ['user','delivery_type','address','phone', 'total_price']
#
#
# class OrderProduct(models.Model):
#     order = models.ForeignKey(Successful_Transaction, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     price = models.FloatField()
#     amount = models.FloatField()
#     order_time = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.product.product_name_geo, self.product.product_ider.name, self.product.product_name_geo, self.product.product_id, self.price, self.quantity, self.total_price, self.order_time