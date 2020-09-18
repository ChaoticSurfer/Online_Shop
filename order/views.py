# from django.shortcuts import render
# from .models import SuccessfulTransaction
# from django.http import HttpResponse
#
#
# def incomeForADmin(request):
#     # info = SuccessfulTransaction.objects.raw(
#     #         "SELECT sum(total_price) FROM order_SuccessfulTransaction GROUP BY transaction_time")
#     # return HttpResponse(b'hi')
#     html = "<html><body>It is now </body></html>"
#     return HttpResponse("wrong")

from django.db import connection
from .models import SuccessfulTransaction, OrderForm, OrderProduct
from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# def incomeForADmin(request):
#     with connection.cursor() as cursor:
#         cursor.execute(r'''SELECT sum(total_price), Count(transaction_id) FROM order_SuccessfulTransaction GROUP BY strftime("%YYYY/%mm", transaction_time)''')
#         row = "\n".join(list(cursor.fetchall()))
#
#     return HttpResponse(str(row), content_type="text/plain")

@login_required(login_url='/login')
def orderproduct(request):
    current_user = request.user
    if request.method == 'POST':  # if there is a post
        form = OrderForm(request.POST)
        #return HttpResponse(request.POST.items())
        if form.is_valid():
            # Send Credit card to bank,  If the bank responds ok, continue, if not, show the error
            # ..............

            data = SuccessfulTransaction()
            # data.first_name = form.cleaned_data['first_name'] #get product quantity from form
            # data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.delivery = form.cleaned_data['delivery']
            # data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total_price = form.cleaned_data['total_price']
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode= get_random_string(5).upper() # random cod
            data.order_code =  ordercode
            data.save() #


    #         for rs in shopcart:
    #             detail = OrderProduct()
    #             detail.order_id     = data.id # Order Id
    #             detail.product_id   = rs.product_id
    #             detail.user_id      = current_user.id
    #             detail.quantity     = rs.quantity
    #             if rs.product.variant == 'None':
    #                 detail.price    = rs.product.price
    #             else:
    #                 detail.price = rs.variant.price
    #             detail.variant_id   = rs.variant_id
    #             detail.amount        = rs.amount
    #             detail.save()
    #             # ***Reduce quantity of sold product from Amount of Product
    #             if  rs.product.variant=='None':
    #                 product = Product.objects.get(id=rs.product_id)
    #                 product.amount -= rs.quantity
    #                 product.save()
    #             else:
    #                 variant = Variants.objects.get(id=rs.product_id)
    #                 variant.quantity -= rs.quantity
    #                 variant.save()
    #             #************ <> *****************
    #
    #         ShopCart.objects.filter(user_id=current_user.id).delete() # Clear & Delete shopcart
    #         request.session['cart_items']=0
    #         messages.success(request, "Your Order has been completed. Thank you ")
    #         return render(request, 'Order_Completed.html',{'ordercode':ordercode,'category': category})
    #     else:
    #         messages.warning(request, form.errors)
    #         return HttpResponseRedirect("/order/orderproduct")
    #
    # form= OrderForm()
    # profile = UserProfile.objects.get(user_id=current_user.id)
    # context = {'shopcart': shopcart,
    #            'category': category,
    #            'total': total,
    #            'form': form,
    #            'profile': profile,
    #            }
    return render(request, 'Order_Form.html', context)