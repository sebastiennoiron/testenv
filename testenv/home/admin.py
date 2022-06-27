from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from testenv.home.models import DataZone, Farm, Farmer, Plot, ProjectManager, RegionalManager,Salesman, TechSupport

# # Register your models here.
# admin.site.register(Farmer)
# admin.site.register(Salesman)
# admin.site.register(RegionalManager)
# admin.site.register(TechSupport)
# admin.site.register(ProjectManager)
from .forms import CustomUserCreationForm, CustomUserChangeForm
from testenv.home.models import DataZone, Farm,Plot,CustomUser
# from testenv.settings import AUTH_USER_MODEL


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username','role','manager', 'is_staff', 'is_active',)
    list_filter = ('username','role','manager', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username','role','manager', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','role','manager', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('role',)
    ordering = ('role',)


admin.site.register(Farm)
admin.site.register(Plot)
admin.site.register(DataZone)
admin.site.register(CustomUser,CustomUserAdmin)