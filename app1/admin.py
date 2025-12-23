from django.contrib import admin
from .models import CustomToken

@admin.register(CustomToken)
class CustomTokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created', 'origin')
    fields = ('user', 'origin',) 