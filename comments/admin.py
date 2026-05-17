from django.contrib import admin
from .models import Comment, Like

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'review', 'content', 'created_at']
    search_fields = ['user__nickname', 'content']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'review', 'created_at']
