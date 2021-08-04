from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Shopkeeper(User):

    shopkeeper_name = models.CharField(max_length=100)
    shopkeeper_address = models.CharField(max_length=100)
    shopkeeper_contact_no = models.IntegerField()
    shopkeeper_status = models.BooleanField(default=False)
    adhar_card = models.CharField(max_length=16)
    gst_number = models.CharField(max_length=100)
    #gender = models.CharField(max_length=10,
    #            choices=(('Male' , 'Male'),
    #            ('Female' , 'Female')))


    class Meta:
        db_table = 'shopkeeper'



class Customer(User):

    phone = models.IntegerField()



    class Meta:
        db_table = "customer"

    def get_cart_count(self):
        try:
            cart = self.customer_cart.get(is_paid = False)
            return cart.cart.count()
        except Exception as e:
            return 0
        return 0        