from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.




class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'date_joined','is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('-date_joined',)
    # search_fields = ('email', 'username', 'first_name', 'last_name')

    # fieldsets = (
    #     (None, {'fields': ('email', 'username', 'password')}),
    #     ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number')}),
    #     ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active', 'is_superuser')}),
    #     ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    # )

   
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
