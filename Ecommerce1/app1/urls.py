from django.urls import path
from .import views

urlpatterns = [    
    path('master/', views.master),
    path('', views.home),

    path('signin/', views.signin,name="signin"),
    path('signup/', views.signup,name="signup"),
    path('signupAuthentication/', views.signupAuthentication,name="signupAuthentication"),
    path('signout/', views.signout,name="signout"),
    path('forgot_password/',views.forgot_password,name="forgot_password"),
    path('forgotOtp/',views.forgotOtp,name="forgotOtp"),
    path('newpassword/',views.newpassword,name='newpassword'),

    path('product/', views.product,name="product"),
    path('productdetail/<int:pk>', views.productdetail,name="productdetail"),


    path('addtocart/<int:pk>/',views.add_to_cart,name="addtocart"),
    path('showmycart/',views.show_mycart,name="showmycart"),

    #path('cart_update/<int:id>/',views.cart_update,name="cart_update"),
    #path('cart_remove/<int:id>/',views.cart_remove,name="cart_remove"),
    #path('deleteitem/<int:id>/',views.remove_items, name='deleteitem'),

]
