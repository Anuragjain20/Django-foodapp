from django.urls import path

from orders import views
urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add-cart/<menu_id>/' , views.add_cart  , name="add_cart"),
        path('sub-cart/<menu_id>/' , views.sub_cart , name="sub_cart"),
          path('rem-cart/<menu_id>/' , views.rem_cart , name="rem_cart"),
        path('payment-successfull/' , views.payment_successfull , name="payment_successfull"),
                path('failure/' , views.failure , name="failure")
]
