from django.contrib import admin
from .models import Post
from ali.models import PostComment

# Register your models here.

admin.site.register((Post, PostComment))