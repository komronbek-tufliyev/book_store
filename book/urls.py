from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage,name='login'),
    path('viewcart/', views.viewcart,name='viewcart'),
    path('addbook/', views.addbook,name='addbook'),
    path('register/', views.registerPage,name='register'),
    path('logout/', views.logoutPage,name='logout'),
    path('addtocart/<str:pk>', views.addtocart,name='addtocart'),
]