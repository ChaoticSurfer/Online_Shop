from django.contrib import admin
from django.db.models import Sum

# Register your models here.
from order.models import SuccessfulTransaction, OrderProduct

class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product', 'price', 'quantity', 'total_price')
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_filter = ['user']
    readonly_fields = ('user', 'transaction_id', 'transaction_time', 'phone', 'delivery', 'address', 'total_price', 'ip')
    can_delete = False
    inlines = [OrderProductline]

    def has_add_permission(self, request):
        return False

class OrderProductAdmin(admin.ModelAdmin):
    list_filter = ['user']




admin.site.register(SuccessfulTransaction, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
