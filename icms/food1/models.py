# # food_app/models.py
#
# from django.db import models
#
# class FoodItem(models.Model):
#     state = models.CharField(max_length=100)
#     famous_foods = models.TextField()
#     average_price = models.DecimalField(max_digits=8, decimal_places=2)
#     # images = models.ImageField(upload_to='food_images/')  # 'upload_to' specifies the directory where images will be stored
#     def _str_(self):
#         return self.state

#//////////////////////////////////////////////////////
from django.db import models

# class FoodItemImage(models.Model):
#     image_url = models.URLField()
#
# class FoodItem(models.Model):
#     state = models.CharField(max_length=100)
#     famous_foods = models.TextField()
#     average_price = models.DecimalField(max_digits=8, decimal_places=2)
#     images = models.ManyToManyField(FoodItemImage)
#
#     def _str_(self):
#         return self.state
#////////


from django.db import models

class FoodItem(models.Model):
    state = models.CharField(max_length=100)
    famous_foods = models.TextField()
    average_price = models.DecimalField(max_digits=8, decimal_places=2)
    image_url = models.URLField(default='https://example.com/default_image.jpg')  # Set the default value

    def _str_(self):
        return self.state
