
from django.urls import path
from app_txt import views
urlpatterns = [
    path('',views.home,name='home.html'),
    path('login',views.register,name='register.html'),
    path('data',views.login,name='data.html'),
]