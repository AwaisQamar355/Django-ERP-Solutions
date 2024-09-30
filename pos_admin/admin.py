from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(AdminUser)
class AdminUser(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'date_joined')
    list_filter = ('is_active', 'date_joined')
    actions = ['activate_users', 'deactivate_users']

    def activate_users(self, request, queryset):
        queryset.update(is_active=True)

    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)

    activate_users.short_description = "Activate selected users"
    deactivate_users.short_description = "Deactivate selected users"

admin.site.register(EmailLog)
admin.site.register(Company)
admin.site.register(Payment)  