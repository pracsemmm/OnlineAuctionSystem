from django.urls import path
from . import views
app_name='first_app'
urlpatterns = [
        path('',views.index,name='index'),
        path('signup/',views.user_signup,name="signup"),
        path('login/',views.user_login,name='login'),
        path('customer_dashbord/',views.customer_dashbord,name='customer_dashbord'),
        path('logout/',views.user_logout,name='user_logout'),
        path('seller_signup/',views.seller_signup,name="seller_signup"),
        path('seller_login/',views.seller_login,name='seller_login'),
        path('seller_dashbord/',views.seller_dashbord,name='seller_dashbord'),
        path('seller_logout/',views.seller_logout,name='seller_logout'),
        path('product_adder_page/',views.product_adder_page,name='product_adder_page'),
        path('input_bid_value/',views.input_bid_value,name='input_bid_value'),
]
