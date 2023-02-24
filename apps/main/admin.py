from django.contrib import admin
from apps.main.models import Page, ProductSet
from adminsortable2.admin import SortableAdminMixin
# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass

class ProductSetProductInline(admin.TabularInline):
    model = ProductSet.products.through
    extra = 1

@admin.register(ProductSet)
class ProductSetAdmin(SortableAdminMixin,admin.ModelAdmin):
    inlines = [ProductSetProductInline]
    fields = ['name','sort','si_active']