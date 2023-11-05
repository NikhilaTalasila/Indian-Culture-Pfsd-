from django.db import models

class Culture(models.Model):
    name = models.CharField(max_length=100)
    external_url = models.URLField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='subcategories')

    def __str__(self):
        return self.name
