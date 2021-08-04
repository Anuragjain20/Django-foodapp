from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from shop.models import Restraunt,RestrauntMenu
# Create your views here.
@login_required(url = "/accounts/shopkeeper_login")
def shop_menu(request,menu_id):
    restraunt = RestrauntMenu.objects.get(id=menu_id)
    pass



@login_required(url = "/accounts/shopkeeper_login")
def shopkeeper_profile(request):
    try :
        shopkeeper = request.user.shopkeeper
        restraunts = RestrauntMenu.objects.get(shopkeeper = shopkeeper)
        pass



