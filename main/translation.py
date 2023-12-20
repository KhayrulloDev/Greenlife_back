from modeltranslation.translator import TranslationOptions, register
from main.models.category import Category
from main.models.product import Product


@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ('name',)


@register(Product)
class ProductTranslation(TranslationOptions):
    pass
