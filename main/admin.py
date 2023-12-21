from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from main.models import Category, Product, File, Order, Partner, Blog


# INLINE
class FileInline(admin.TabularInline):
    model = File
    fields = ('file',)


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'parent_id')


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'price', 'category_id')

    inlines = (FileInline,)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'product_id', 'count')


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')


@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'description')

