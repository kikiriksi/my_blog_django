from django.contrib import admin
from .models import Post, CommentsModel


# Register your models here.
@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'author',)  # отоброжение полей


@admin.register(CommentsModel)
class AdminComents(admin.ModelAdmin):
    list_display = ('comments',)
