from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return str(self.name) 
    def get_absolute_url(self):
        #return reverse('detail_view',args=(str(self.id)))
        return reverse('home_view')
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blogs')
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255,default='Personal')

    def __str__(self):
        return str(self.title) + '    '+ str(self.author)
    def get_absolute_url(self):
        #return reverse('detail_view',args=(str(self.id)))
        return reverse('home_view')
