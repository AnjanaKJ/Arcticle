from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    name=models.CharField(max_length=25,blank=True,null=True)
    email = models.EmailField(default="abcd@gmail.com")
    des = models.TextField(default="Write article .",null = False)

def get_absolute_url(self):
    return reverse("det", kwargs={"id": self.id})
