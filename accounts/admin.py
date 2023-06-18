from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'date_joined', 'last_login', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name', 'username')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    ordering = ('-date_joined',)
    readonly_fields = ['password', 'last_login', 'date_joined']

admin.site.register(Account, AccountAdmin)