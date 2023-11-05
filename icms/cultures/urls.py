from django.urls import path
from . import views

urlpatterns = [
    path('cultures/', views.culture_list, name='culture_list'),
    path('cultures/<int:culture_id>/', views.culture_list, name='culture_list'),
]
