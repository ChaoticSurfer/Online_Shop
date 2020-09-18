# from decimal import Decimal
# from django.conf import settings
# from shop.models import Product
#
# class Cart(object):
#     def __init__(self, request):
#         """
#         Initialize the cart.
#         """
#         self.session = request.session
#         cart = self.session.get(settings.CART_SESSION_ID)
#         if not cart:
#             # save an empty cart in the session
#             cart = self.session[settings.CART_SESSION_ID] = {}
#         self.cart = cart
#
#     def add(self, product, quantity=1, update_quantity=False):
#         """
#         Add a product to the cart or update its quantity.
#         """
#         product_id = str(product.product_id)
#         if product_id not in self.cart:
#             self.cart[product_id] = {'quantity': 0, 'name_geo': product.product_name_geo,'name_eng': product.product_name_eng,'name_rus': product.product_name_rus,
#                                      'price': str(product.price)}
#         if update_quantity:
#             self.cart[product_id]['quantity'] = quantity
#         else:
#             self.cart[product_id]['quantity'] += quantity
#         self.save()
#
#     def save(self):
#
#         # update the session cart
#         self.session[settings.CART_SESSION_ID] = self.cart
#         # mark the session as "modified" to make sure it is saved
#         self.session.modified = True
#
#     def remove(self, product):
#         """
#         Remove a product from the cart.
#         """
#         product_id = str(product.product_id)
#         if product_id in self.cart:
#             del self.cart[product_id]
#         self.save()
#
#     def __iter__(self):
#         """
#         Iterate over the items in the cart and get the products
#         from the database.
#         """
#
#         product_ids = self.cart.keys()
#         # get the product objects and add them to the cart
#         products = Product.objects.filter(id__in=product_ids)
#         for product in products:
#             self.cart[str(product.id)]['product'] = product
#         for item in self.cart.values():
#             item['price'] = Decimal(item['price'])
#             item['total_price'] = item['price'] * item['quantity']
#             yield item
#
#     def __len__(self):
#         """
#         Count all items in the cart.
#         """
#
#         return sum(item['quantity'] for item in self.cart.values())
#
#     def get_total_price(self):
#         return sum(Decimal(item['price']) * item['quantity'] for item in
#                    self.cart.values())
#
#     def clear(self):
#
#         # remove cart from session
#         del self.session[settings.CART_SESSION_ID]
#         self.session.modified = True


from decimal import Decimal
from django.conf import settings
from shop.models import Product
import json
from shop.views import get_products

class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        id = str(product.id)
        if id not in self.cart:
            self.cart[id] = {'quantity': 0, 'name_geo': product.product_name_geo,
                             'name_eng': product.product_name_eng, 'name_rus': product.product_name_rus,
                             'image': '/media/'+str(product.image_low_quality),
                             'price': str(product.price), 'limit': product.amount_in_warehouse, 'total_price': 0, 'weight':str(product.weight)}
        if update_quantity:
            self.cart[id]['quantity'] = quantity
            self.cart[id]['total_price'] = str(self.cart[id]['quantity'] * Decimal(self.cart[id]['price']))
        else:
            if self.cart[id]['quantity'] < product.amount_in_warehouse:
                self.cart[id]['quantity'] += quantity
                self.cart[id]['total_price'] = str(self.cart[id]['quantity'] * Decimal(self.cart[id]['price']))
        self.save()

    def substract(self, product, quantity=1, update_quantity=False):
        '''
        substract a product to the cart or u    update its quantity.
        '''
        id = str(product.id)
        if update_quantity:
            self.cart[id]['quantity'] = quantity
        else:
            if id in self.cart:
                if self.cart[id]['quantity'] == 1 or self.cart[id]['quantity'] < 1:
                    self.remove(product)
                else:
                    self.cart[id]['quantity'] -= 1
        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        id = str(product.id)
        if id in self.cart:
            del self.cart[id]
            self.save()

    # needs check
    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        # products = Product.objects.filter(product_id__in=product_ids)
        products = [i for i in Product.objects.all() if i.id in product_ids]
        # products = [i for i in Product.objects.all() if i.product_id in product_ids]
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

        '''
        {1: {'quantity': 0, 'name_geo': 'product.product_name_geo', 'name_eng': 'product.product_name_eng',
              'name_rus': 'product.product_name_rus', 'image': 'json.dumps(str(product.image_low_quality))',
              'price': 'str(product.price)'}}
        '''

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    # def total_price(self):
    #     return (Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def get_total_weight(self):
        return sum(Decimal(item['weight']) * item['quantity'] for item in self.cart.values())

    def get_total_amount(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True