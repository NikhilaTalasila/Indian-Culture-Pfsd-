# from django.db import models
#
# class City(models.Model):
#     name = models.CharField(max_length=100)
#     external_url = models.URLField()
#
#     def __str__(self):
#         return self.name

from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    external_url = models.URLField()
    image_url = models.URLField(default='https://example.com/default-image.jpg')  # Add a field with a default value

    def __str__(self):
        return self.name

