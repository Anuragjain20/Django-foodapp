

# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from shop.models import Restraunt,RestrauntMenu


def index(request):
    print(request.user)
    context = {'restraunts' : Restraunt.objects.all()}
  
    return render(request, 'home/index.html',context)


def restraunt_menu(request,slug):
    try:
        restraunt_obj = Restraunt.objects.get(id = slug)
        context = {'restraunt' :restraunt_obj , 'restraunts_menu' : restraunt_obj.restraunt.all()}
        return render(request, 'home/resturant_menu.html',context)
    except Exception as e:
        print(e)

    return redirect('/')

    
