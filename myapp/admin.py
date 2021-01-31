from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Categories
#đăng ký model student với admin
admin.site.register(Post)
admin.site.register(Categories)
