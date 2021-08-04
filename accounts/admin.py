from django.contrib import admin

# Register your models here.
from accounts.models import Shopkeeper,Customer

admin.site.register(Shopkeeper)
admin.site.register(Customer)