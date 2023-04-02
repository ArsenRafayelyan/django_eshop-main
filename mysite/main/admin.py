from django.contrib import admin
from .models import HomeSlider, HomeSliderActive, Category, SubCategory, Product, Category_Product
# Register your models here.

@admin.register(HomeSlider, HomeSliderActive)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name1', 'name2']
    list_display_links = ['id', 'name1']
    search_fields = ['name1']

@admin.register(Category, SubCategory, Category_Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']