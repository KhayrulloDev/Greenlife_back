from modeltranslation.translator import TranslationOptions, register

from main.models import Blog
from main.models.category import Category
from main.models.product import Product


@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ('name',)


@register(Product)
class ProductTranslation(TranslationOptions):
    fields = ('name', 'category', 'description')


@register(Blog)
class BlogTranslation(TranslationOptions):
    fields = ('title', 'description')
