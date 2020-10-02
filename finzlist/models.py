from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Bookmark(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    site_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    url = models.URLField('Site URL')
    votes = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ['updated']

    def __str__(self):
        return self.site_name 

    def get_absolute_url(self):
        return reverse("detail", args=[str(self.id)])

    





