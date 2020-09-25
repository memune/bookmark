from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    url = models.URLField('Site URL')
    votes = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.site_name

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])

    def get_queryset(self):
        return Bookmark.objects.order_by('-votes')




