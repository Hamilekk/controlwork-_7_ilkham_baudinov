from django.contrib import admin

from webapp.models import GuestBook


# Register your models here.

class AdminGuestBook(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'status',  'created_at']
    list_filter = ['name']
    search_fields = ['name', 'email', 'status']
    fields = ['name', 'email', 'text', 'status', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(GuestBook, AdminGuestBook)
