from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post (models.Model):
    title = models.CharField(max_length=40, help_text='최대 40자 내로 입력가능합니다.')
    content = models.TextField(verbose_name='주관기관')

    deadline = models.DateTimeField()
    tag = models.CharField(max_length=100, blank=True)

    autor = models.ForeignKey(User, on_delete=True)

    def __str__(self):
        return '{}::{}'.format(self.title.self.deadline)
