from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'nickname', 'is_staff', 'created_at']
    fieldsets = UserAdmin.fieldsets + (
        ('추가 정보', {'fields': ('nickname',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('추가 정보', {'fields': ('email', 'nickname')}),
    )
