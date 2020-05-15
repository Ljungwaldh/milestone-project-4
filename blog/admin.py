from django.contrib import admin

from .models import BlogArticle, Comment

admin.site.register(BlogArticle)
admin.site.register(Comment)
