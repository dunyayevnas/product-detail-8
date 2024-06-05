from django.contrib import admin
from .models import *


@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'created_at')
    list_filter = ('name', 'created_at')


@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'created_at')
    list_filter = ('name', 'created_at')

class ProductImageModelAdmin(admin.StackedInline):
    model = ProductImageModel

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'created_at')
    list_filter = ('created_at',)
    inlines = [ProductImageModelAdmin]


@admin.register(ProductSizeModel)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'created_at')
    list_filter = ('created_at',)


@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'created_at')
    list_filter = ('created_at',)


@admin.register(ProductManufacture)
class ProductManufactureAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'created_at')
    list_filter = ('created_at',)


