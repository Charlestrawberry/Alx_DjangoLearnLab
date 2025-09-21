from django.contrib import admin
# import the book model
from .models import Book, User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("publication_year",)



@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_of_birth')
    fieldsets = BaseUserAdmin.fieldsets + (
        (_('Profile'), {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (_('Profile'), {'fields': ('date_of_birth', 'profile_photo')}),
    )