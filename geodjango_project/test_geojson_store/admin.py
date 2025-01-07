from django.contrib import admin
from .models import Territorie, FileUpload, CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
        'tanar', 'tanulo')
    fieldsets = UserAdmin.fieldsets + (
        ('További mezők', {'fields': ('tanar', 'tanulo')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('További mezők', {'fields': ('tanar', 'tanulo')}),
    )

admin.site.register(Territorie)
admin.site.register(FileUpload)
admin.site.register(CustomUser, CustomUserAdmin)

