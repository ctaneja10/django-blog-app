from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    number = models.IntegerField(max_length=20, default="")
    txt = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Blog(models.Model):
    blog_slug = models.IntegerField(default=0)
    blog_title = models.CharField(max_length=100, default="")
    blog_sub_heading = models.CharField(max_length=200, default="")
    blog_sub_heading1 = models.CharField(max_length=50, default="")
    blog_content = models.TextField(max_length=5000, default="")
    blog_pub_date = models.DateField()

    def __str__(self):
        return self.blog_title







