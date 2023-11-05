# food_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...

    path('food/', views.food_list, name='food_list'),
]
