from rest_framework.serializers import ModelSerializer

from .models import Partner, Product
from .models import Partner, Product, Order

from .models import Partner, Product, Order, Category
from .models.feedback import Feedback
from .models.reviews import Review

from .models import Partner, Blog


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'parent_id')


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'image')


class BlogListSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class ProductPriceListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'organization', 'category', 'price')


class ProductWithCategory(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'productivity')


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
