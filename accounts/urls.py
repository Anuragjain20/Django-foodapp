from django.urls import path
from accounts import views



urlpatterns = [

        path('register/', views.register, name='register'),
        path('login/', views.login, name='login'),
    path('shopkeeper_register/', views.shopkeeper_register, name='shopkeeper_register'),
        path('shopkeeper_login/', views.shopkeeper_login, name='shopkeeper_login'),
        path('logout/', views.signout,name='logout'),
]
