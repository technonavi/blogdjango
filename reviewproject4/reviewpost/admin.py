from django.contrib import admin
from .models import ReviewModel,Category,FileModel
admin.site.register(ReviewModel)
admin.site.register(Category)
# Register your models here.

admin.site.register(FileModel)