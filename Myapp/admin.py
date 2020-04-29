from django.contrib import admin
from .models import BookModel, UserModel

# Register your models here.


admin.site.register(BookModel)
admin.site.register(UserModel)