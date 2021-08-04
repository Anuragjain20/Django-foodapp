from django.urls import path

from home import views
urlpatterns = [
    path('', views.index, name='index'),
    path('menu/<slug>/', views.restraunt_menu, name='menu'),
]
