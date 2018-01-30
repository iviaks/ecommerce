from django.contrib import admin
from catalog.models import Product, Store


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    pass
