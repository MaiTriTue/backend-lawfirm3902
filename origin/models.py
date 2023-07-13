from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# from ckeditor.fields import RichTextField

class TagField(models.Model):
    class Meta:
        ordering = ['id']
    name = models.CharField(max_length=255,  null=False, unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):

    class Meta:
        ordering = ['id']

    avatar = models.ImageField(upload_to='upload/%Y/%m')
    position = models.CharField(max_length=255,  null=False)
    field = models.CharField(max_length=255,  null=False)
    experience = models.CharField(max_length=255,  null=False)
    level = models.CharField(max_length=255,  null=False)
    phone = models.CharField(max_length=10,  null=False)
    tagsField = models.ManyToManyField('TagField', blank=True, null=True, related_name='tagfields')



class Category(models.Model):
    class Meta:
        ordering = ['id']

    name = models.CharField(max_length=255,  null=False, unique=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    class Meta:
        ordering = ['id']

    name = models.CharField(max_length=255, null=False, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Posts(models.Model):
    class Meta:
        ordering = ['id']

    title = models.CharField(max_length=255, null=False)
    # disc = RichTextField()
    disc = models.TextField(max_length=255, null=False)
    image = models.CharField(max_length=255, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    # content = RichTextField()
    content = models.TextField(max_length=255, null=False)
    file_upload = models.FileField(upload_to='fileUpload/%Y/%m')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Contact(models.Model):
    class Meta:
        ordering = ['id']

    name = models.CharField(max_length=255, null=False)
    area = models.CharField(max_length=255, null=False)
    address = models.TextField(max_length=255, null=False)
    phone = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

class Introduce(models.Model):
    class Meta:
        ordering = ['id']

    name = models.CharField(max_length=255, null=False)
    manager = models.CharField(max_length=255, null=False)
    # content = RichTextField()
    content = models.TextField(max_length=255, null=False)


    def __str__(self):
        return self.name

# Create your models here.







