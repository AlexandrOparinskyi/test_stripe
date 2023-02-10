from django.contrib import admin

from .models import Items


class ItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']


admin.site.register(Items, ItemsAdmin)
