# from django.db import models
#
# class State(models.Model):
#     name = models.CharField(max_length=100, unique=True)
#
#     def __str__(self):
#         return self.name
#
# class FamousFood(models.Model):
#     state = models.ForeignKey(State, on_delete=models.CASCADE)
#     food_name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.food_name
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    external_url = models.URLField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)  # Add a field for the image URL
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='subcategories')

    def _str_(self):
        return self.name




