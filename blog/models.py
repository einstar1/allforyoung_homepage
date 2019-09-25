from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name_plural = 'categories'
        

        
class Post (models.Model):
    Category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='카테고리')

    title = models.CharField(max_length=40, verbose_name='대외활동명')
    organization = models.CharField(max_length=20, verbose_name='주관기관')

    image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True, verbose_name='이미지')

    birthline = models.DateField(verbose_name='시작날짜')
    deadline = models.DateTimeField(verbose_name='마감날짜')
  
   
    tag = models.CharField(max_length=100, blank=True, verbose_name='태그')
    
    link = models.TextField(verbose_name='링크')

    author = models.ForeignKey(User, on_delete=True, verbose_name='등록자')
    created = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)
