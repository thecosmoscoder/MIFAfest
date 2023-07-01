from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    ''' Creation Form'''
    add_form = CustomUserCreationForm 
    add_fieldsets = UserAdmin.add_fieldsets + ( 
        (None, {'fields': ('age', 'country',)}),
    )
    ''' Change Form '''
    form = CustomUserChangeForm  
    fieldsets = UserAdmin.fieldsets + (  
        (None, {'fields': ('age', 'country',)}),
    )
    ''' List of fileds that display in Users administration '''
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
    )


admin.site.register(CustomUser, CustomUserAdmin)
