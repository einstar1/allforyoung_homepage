from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length=40, verbose_name='제목')
    organization = models.CharField(max_length=20, verbose_name='주관기관')

    birthline = models.DateField(verbose_name='시작날짜')
    deadline = models.DateTimeField(verbose_name='마감날짜')

    tag = models.CharField(max_length=100, blank=True, verbose_name='태그')

    autor = models.ForeignKey(User, on_delete=True, verbose_name='등록자')
    created = models.DateTimeField(auto_now_add=True, verbose_name='등록일')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}::{}'.format(self.title, self.deadline)
