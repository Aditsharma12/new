from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'message')
    search_fields = ('email', 'phone')
    list_filter = ('email', 'phone')

# Alternatively, you can use the standard registration method:
# admin.site.register(Contact, ContactAdmin)
