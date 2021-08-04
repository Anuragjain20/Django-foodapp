from django.shortcuts import render,redirect

# Create your views here.
from accounts.models import Shopkeeper,Customer
# import messages
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login


def shopkeeper_register(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')
        address = request.POST.get('address')
        addhar = request.POST.get('addhar')
        phone = request.POST.get('phone')
        gst = request.POST.get('gst')
       # gender = request.POST.get('gender')

        if Shopkeeper.objects.filter(email=email).first():
            messages.warning(request, 'Already registered with this email') 
            
            return render(request, 'accounts/register_shopkeeper.html')

        if Shopkeeper.objects.filter(username=username).first():
            messages.warning(request, 'Already registered with this email')
            return render(request, 'accounts/register_shopkeeper.html')





        shopkeeper = Shopkeeper.objects.create(
            username = username,
            email = email,
            shopkeeper_name = name,
     
            shopkeeper_address =address,
            shopkeeper_contact_no = phone,
            adhar_card = addhar,
            gst_number = gst,          

            )
        shopkeeper.set_password(password)
        shopkeeper.save()
     
        return redirect('../shopkeeper_login')
        #return render(request, 'accounts/register_shopkeeper.html')
   
    return render(request, 'accounts/register_shopkeeper.html')

def shopkeeper_login(request):
    try:
            
        if request.method == 'POST':
            username = request.POST.get('email')
            password= request.POST.get('password')

            if not username or not password:
                messages.warning(request, 'Already registered with this email')
                return redirect('/accounts/shopkeeper_login')
            shopk_objs=Shopkeeper.objects.filter(username=username).first()
            if shopk_objs is None:
                messages.warning(request, 'Already registered with this email')
                return redirect('/accounts/shopkeeper_login')
            
            user=authenticate(username=username,password=password)

            if user is None:
                messages.warning(request, 'error')
                return redirect('/accounts/shopkeeper_login')
            print("logged in")
            login(request,user)
      
            return redirect('/')
    except Exception as e:
        print(e)
   
    return render(request,'accounts/login_shopkeeper.html')




def register(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('email')
            password= request.POST.get('password')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
        if Customer.objects.filter(email=email).first():
            messages.warning(request, 'Already registered with this email')
            
            return render(request, 'accounts/register.html')

        if Customer.objects.filter(username=username).first():
            messages.warning(request, 'Already registered with this email')            
            return render(request, 'accounts/register.html')

        customer = Customer.objects.create(username=username,email=email,phone=phone)    
        customer.set_password(password)
        customer.save()
        return redirect('/accounts/login')

    except Exception as e:
        print(e)
       
    return render(request,'accounts/register.html')
    
def login(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('email')
            password= request.POST.get('password')
            if not username or not password:
                messages.error(request, 'error')                  
                return redirect('/accounts/login')
            
            shopk_objs=Customer.objects.filter(username=username).first()
            if shopk_objs is None:
                messages.error(request, 'error')                  
                return redirect('/accounts/login')
            user=authenticate(username=username,password=password)
            if user is None:
                messages.error(request, 'error')                  
                return redirect('/accounts/login')
            print("logged in")
            auth_login(request,user)
 
            return redirect('/')
    except Exception as e:
        print(e)
    return render(request,'accounts/login.html')


def signout(request):
    logout(request)
    return redirect('/')