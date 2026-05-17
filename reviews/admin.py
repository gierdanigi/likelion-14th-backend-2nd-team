from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'movie', 'rating', 'created_at']
    list_filter = ['rating']
    search_fields = ['title', 'user__nickname', 'movie__title']
