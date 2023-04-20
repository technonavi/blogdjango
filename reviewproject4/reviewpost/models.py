from django.db import models
from django.contrib.auth.models import User

EVALUATION_CHOICES=[('良い','良い'),('悪い','悪い')]
class Category(models.Model):
    name = models.CharField('カテゴリー', max_length=50)
    class Meta:
            db_table = 'categories'
    def __str__(self):
      return self.name
class ReviewModel(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    images=models.ImageField(upload_to='')
    useful_review=models.IntegerField(null=True,blank=True,default=0)
    evaluation=models.CharField(max_length=10,choices=EVALUATION_CHOICES)
class FileModel(models.Model):
  title = models.CharField(max_length=100)
  uploadplace = models.FileField(upload_to='upload/')
