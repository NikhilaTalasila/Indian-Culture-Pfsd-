# # food_app/views.py
#
# from django.shortcuts import render
# from .models import FoodItem
#
# def food_list(request):
#     food_items = FoodItem.objects.all()
#     return render(request, 'food/food_list.html', {'food_items': food_items})


# food_app/views.py

from django.shortcuts import render
from .models import FoodItem

def food_list(request):
    food_items = FoodItem.objects.all()
    return render(request, 'food1/food_list.html', {'food_items': food_items})
