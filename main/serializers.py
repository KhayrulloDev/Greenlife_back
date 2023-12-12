from rest_framework.serializers import ModelSerializer
from .models import Partner, Product, Order
from .models.feedback import Feedback
from .models.reviews import Review


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
        fields = ('id', 'name', 'organization', 'category', 'price')


class ProductWithCategory(ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'productivity', 'growth_zone', 'data_json')


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
