# from django.shortcuts import render
# from .models import State, FamousFood
#
# # Create your views here.
# def state_foods_table(request):
#     states = State.objects.all()
#     data = []
#
#     for state in states:
#         foods = FamousFood.objects.filter(state=state)
#         data.append({'state': state, 'foods': foods})
#
#     return render(request, 'food/state_foods_table.html', {'data': data})
#
# def food(request):
#
#     return render(request,"food/food.html")
# def mfood(request):
#     return render(request,template_name="food/mfood.html")
# def kfood(request):
#     return render(request,template_name="food/kfood.html")
# def tfood(request):
#     return render(request,template_name="food/tfood.html")
from django.shortcuts import render, redirect
from .models import Category

def category_list(request, category_id=None):
    if category_id is None:
        categories = Category.objects.filter(parent_category__isnull=True)
        return render(request, 'food/category_list.html', {'categories': categories})
    else:
        category = Category.objects.get(pk=category_id)
        if category.external_url:
            return redirect(category.external_url)
        else:
            subcategories = category.subcategories.all()
            return render(request, 'food/category_list.html', {'categories': subcategories})




