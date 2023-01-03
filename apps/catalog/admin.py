from django.contrib import admin
from apps.catalog.models import Category, Product



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":['name']}

class ProductCategoryInline(admin.TabularInline):
    model = Product.categories.through



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['name']}
    inlines = {ProductCategoryInline}