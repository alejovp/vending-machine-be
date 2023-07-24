from django.contrib import admin
from apps.vending.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "created_at", "updated_at"]
    ordering = ["-created_at"]

# class StockAdmin(admin.ModelAdmin):
#     list_display = ["product", "quantity", "created_at", "updated_at"]
#     ordering = ["-created_at"]


admin.site.register(Product, ProductAdmin)
# admin.site.register(Stock, StockAdmin)