from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.models import User 
from django.contrib.auth.admin import UserAdmin 
from .utils import send_login_email
from django.contrib.auth.hashers import make_password

# unregister the default User model 
# admin.site.unregister(User)

# register the CustomUser model with custom fields and methods
class CustomUserAdmin(admin.ModelAdmin):
    #  show only email, role and permissions fields
    list_display = ('username', 'email', 'role', 'is_wmi_domain', 'is_staff', 'is_active')
    search_fields = ('username','email', 'role')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username','email', 'password', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2', 'role')}
        ),
    )
    ordering = ('email',)

    # override save_model to send email when a user is added
    def save_model(self, request, obj, form, change):
        if 'password' in form.changed_data:
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change) # save user first

admin.site.register(CustomUser, CustomUserAdmin)
