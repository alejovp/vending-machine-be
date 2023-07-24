from django.contrib import admin
from apps.vending.models import Product, VendingMachineSlot


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "created_at", "updated_at"]
    ordering = ["-created_at"]

# class StockAdmin(admin.ModelAdmin):
#     list_display = ["product", "quantity", "created_at", "updated_at"]
#     ordering = ["-created_at"]

class VendingMachineSlotAdmin(admin.ModelAdmin):
    list_display = ["product", "quantity", "row", "column"]
    ordering = ["row"]


admin.site.register(Product, ProductAdmin)
admin.site.register(VendingMachineSlot, VendingMachineSlotAdmin)
# admin.site.register(Stock, StockAdmin)