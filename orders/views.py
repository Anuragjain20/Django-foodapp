from django.shortcuts import render,redirect
from orders.models import *
from shop.models import Restraunt,RestrauntMenu
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
import razorpay
from django.conf import settings

client = razorpay.Client(auth=(settings.KEY_ID, settings.KEY_SECRET))
# Create your views here.
def cart(request):

    try:
        cart_obj = Cart.objects.get(customer = request.user.customer , is_paid = False)

        val = cart_obj.total_quantity(cart_obj)
        total_price = cart_obj.total_price_update(cart_obj)        
        payment = client.order.create(
            {'amount' : cart_obj.total_price * 100 , 'currency' : 'INR' , 'payment_capture' :1 }
        )
        cart_obj.razor_pay_order_id = payment['id']
        cart_obj.save()
        
        context = {'carts' : cart_obj , 'order_id':payment['id'] , 'key_id' : settings.KEY_ID,"total_quantity":val,"total_price":total_price}
        
        return render(request , 'cart/cart.html' , context)
    except Exception as e:
        print(e)
    
    return render(request , 'cart/empty.html')
 


@login_required(login_url='/accounts/login/')
def add_cart(request,menu_id) :
    try:
        customer = request.user.customer
        cart_obj,_ =  Cart.objects.get_or_create(customer=customer,is_paid = False)
        menu_obj = RestrauntMenu.objects.get(id=menu_id)

        if cart_obj.cart.filter(restraunt_menu = menu_obj).exists():
            cart_item_obj = CartItems.objects.get(
                cart = cart_obj,
                restraunt_menu = menu_obj)
            cart_item_obj.quantity += 1 
            cart_item_obj.save()
        else:
            CartItems.objects.create(
                cart = cart_obj,
                restraunt_menu =menu_obj )

    except Exception as e:
        print(e)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))        
    

def payment_successfull(request):
    try:
        razor_pay_order_id = request.GET.get('razorpay_order_id')
        razorpay_payment_id = request.GET.get('razorpay_payment_id')
        razorpay_signature = request.GET.get('razorpay_signature')   
        cart_obj = Cart.objects.get(razor_pay_order_id = razor_pay_order_id)
        cart_obj.is_paid = True
        cart_obj.razorpay_payment_id = razorpay_payment_id
        cart_obj.razorpay_signature = razorpay_signature
        cart_obj.save()
        return HttpResponse('Success')
    except Exception as e:
        print(e)
    
    return HttpResponse('Something went wrong')


def sub_cart(request,menu_id):
    try:
        customer = request.user.customer
        cart_obj,_ =  Cart.objects.get_or_create(customer=customer,is_paid = False)
        menu_obj = RestrauntMenu.objects.get(id=menu_id)

        if cart_obj.cart.filter(restraunt_menu = menu_obj).exists():
            cart_item_obj = CartItems.objects.get(
                cart = cart_obj,
                restraunt_menu = menu_obj)
            if cart_item_obj.quantity  > 1:
                cart_item_obj.quantity -= 1 
                cart_item_obj.save() 
            else:       
                cart_item_obj.delete()
          
    


    except Exception as e:
        print(e)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))          

def rem_cart(request,menu_id):

    try:
        customer = request.user.customer
        cart_obj,_ =  Cart.objects.get_or_create(customer=customer,is_paid = False)
        menu_obj = RestrauntMenu.objects.get(id=menu_id)

        if cart_obj.cart.filter(restraunt_menu = menu_obj).exists():
            cart_item_obj = CartItems.objects.get(
                cart = cart_obj,
                restraunt_menu = menu_obj)
            
            cart_item_obj.delete()
    


    except Exception as e:
        print(e)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))       

def failure(request):
    return HttpResponse('Something went wrong')

