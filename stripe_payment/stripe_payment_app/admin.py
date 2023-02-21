from django.contrib import admin

from .models import Item, Order, Tax, Discount


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("pk", "name",)
    list_display_links = ("pk", "name")
    search_fields = ("name",)
    fields = ("name", "description", "price",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("pk",)
    fields = ("items", "tax", "discount",)


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ("pk", "display_name",)
    list_display_links = ("pk", "display_name",)
    search_fields = ("display_name",)
    fields = ("display_name", "inclusive", "percentage",)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ("pk",)
    fields = ("percent_off",)
