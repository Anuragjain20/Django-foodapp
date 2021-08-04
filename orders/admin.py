from django.contrib import admin

# Register your models here.
from orders.models import  Cart,CartItems,CouponCode


admin.site.register([
    Cart,
    CartItems,
    CouponCode,
])