from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("pk", "name",)
    list_display_links = ("pk", "name")
    search_fields = ("name",)
    fields = ("name", "description", "price",)
