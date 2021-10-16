from django.contrib import admin
from .models import (
    Product, 
    Order, 
    OrderItem, 
    BebidaVariation,
    PostreVariation,
    Address,
    Payment,
    Category
)

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'address_line_1',
        'zip_code',
        'city',
        'address_type',
    ]

admin.site.register(Product)
admin.site.register(Address, AddressAdmin)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(BebidaVariation)
admin.site.register(PostreVariation)
admin.site.register(Payment)
admin.site.register(Category)