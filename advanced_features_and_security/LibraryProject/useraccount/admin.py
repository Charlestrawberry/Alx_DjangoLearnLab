from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Extends the stock UserAdmin to include our extra fields in forms and list display.
    """
    # Show in list page
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_of_birth')
    list_filter = BaseUserAdmin.list_filter

    # Add our fields to the standard fieldsets
    fieldsets = BaseUserAdmin.fieldsets + (
        (_('Profile'), {'fields': ('date_of_birth', 'profile_photo')}),
    )

    # Add our fields to the "add user" page
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (_('Profile'), {'fields': ('date_of_birth', 'profile_photo')}),
    )

    search_fields = BaseUserAdmin.search_fields
    ordering = BaseUserAdmin.ordering
