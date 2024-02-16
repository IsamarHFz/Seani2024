from django.contrib import admin

from .models import Career

class CarreerAdmin(admin.ModelAdmin):
    list_display = ['short_name', 'level']
    list_filter = ['level']

# Register your models here.
admin.site.register(Career, CarreerAdmin)