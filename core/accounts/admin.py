from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User , Profile

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email','is_active' , 'is_superuser')
    list_filter =  ("email", "is_staff", "is_active",)
    fieldsets = (
        ('Authentication', {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active",'is_superuser')}),
         ('Groups Permissions', {
                            "classes": ("wide",),
                            "fields": (
                                "groups","user_permissions"
                            )}
                        ),
                ('Important date', {
                                    "classes": ("wide",),
                                    "fields": (
                                        "last_login",
                                    )}
                                ),
    )
    add_fieldsets = (
        ('Authentication', {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active",'is_superuser'
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
# Register your models here.
