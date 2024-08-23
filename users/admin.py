from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from .models import CustomAdminLog

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email',
                    'username',
                    'is_staff',
                    'is_active',
                    ]
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets

admin.site.register(CustomUser, CustomUserAdmin)

# @admin.register(CustomAdminLog)
# class CustomAdminLogAdmin(admin.ModelAdmin):
#     list_display = ['action_time', 'user', 'content_type', 'object_repr', 'action_flag', 'change_message']
# Register your models here.
