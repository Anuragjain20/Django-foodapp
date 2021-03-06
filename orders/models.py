from django.db import models
from home.models import BaseModel
from accounts.models import Customer
from shop.models import RestrauntMenu



class CouponCode(BaseModel):
    coupon_name = models.CharField(max_length=100)
    coupon_code = models.CharField(max_length =100)
    coupon_discount_type = models.CharField(max_length=100 , choices=(('Percentage' , 'Percentage') , ('Amount' , 'Amount')))
    coupon_discount_price = models.IntegerField(default=50)
    

class Cart(BaseModel):
    customer = models.ForeignKey(Customer , related_name='customer_cart' ,  on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    total_price = models.IntegerField(default=0)
    razor_pay_order_id = models.CharField(max_length=1000 , null=True,blank=True)
    razorpay_payment_id = models.CharField(max_length=100 , null=True , blank=True)
    razorpay_signature = models.CharField(max_length=100 , null=True , blank=True)

    def __str__(self) -> str:
        return f'{self.customer.email} | {self.id}'

    def total_quantity(self,obj):
        r = obj.cart.all()
        quant = [i.quantity for i in r]
        if len(quant) == 0:
            return 0
        return sum(quant)


    def total_price_update(self,obj):
        r = obj.cart.all()
        quant = [i.quantity * i.restraunt_menu.menu_price for i in r]
        y =0
        if len(quant ) > 0:
            y= sum(quant) 
        obj.total_price = y
        obj.save()         
        return  y
                


class CartItems(BaseModel):
    cart = models.ForeignKey(Cart , related_name="cart" , on_delete=models.CASCADE)
    restraunt_menu = models.ForeignKey(RestrauntMenu , related_name="cart_restraunt_menu" , on_delete=models.SET_NULL , null=True , blank=True)
    quantity = models.IntegerField(default = 1)


