from rest_framework.serializers import ModelSerializer
from .models import Partner, Product, Order, Category, Blog
from .models.feedback import Feedback
from .models.reviews import Review


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name_en', 'name_uz', 'name_ru', 'parent_id')


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductPriceListSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name_en', 'name_uz', 'name_ru', 'organization', 'category_en', 'category_uz', 'category_ru', 'price')


class ProductWithCategory(ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name_en', 'name_uz', 'name_ru', 'productivity')


class OrderProductSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class FeedBackSerializer(ModelSerializer):

    class Meta:
        model = Feedback
        fields = '__all__'


class ReviewSerializer(ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class BlogSerializer(ModelSerializer):

    class Meta:
        model = Blog
        fields = ('id', 'title_en', 'title_uz', 'title_ru', 'image')


class BlogDetailSerializer(ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'
