from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm, CustomUserChangeForm, GroupAdminForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active',)
    list_filter = ('email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'role', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'role', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email', 'first_name', 'last_name', 'role',)
    ordering = ('email', 'first_name', 'last_name', 'role',)

    def save_model(self, request, obj, form, change):
        sales_team = Group.objects.get(name="Sales team")
        support_team = Group.objects.get(name="Support team")
        if obj.role == "Sales Contact":
            super().save_model(request, obj, form, change)
            obj.groups.add(sales_team)
        elif obj.role == "Support Contact":
            super().save_model(request, obj, form, change)
            obj.groups.add(support_team)


admin.site.register(CustomUser, CustomUserAdmin)

# Unregister the original Group admin.
admin.site.unregister(Group)


# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']


# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)
