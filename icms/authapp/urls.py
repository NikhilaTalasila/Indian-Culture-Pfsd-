# authapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('nav_buttons/', views.nav_buttons, name='nav_buttons'),
    #path('index/',views.index,name='index'),
]
