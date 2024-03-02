from django.urls import path, include

from . import views



urlpatterns = [
    path('', views.loginpage, name="login"),
    path('register/', views.registerpage, name="register"),
    path('logout/', views.logoutPage, name="logout"),

    path('', include('base.urls')),
    


]