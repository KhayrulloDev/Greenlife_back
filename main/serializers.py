from rest_framework.serializers import ModelSerializer
from .models import Partner, Product

from .models import Partner, Blog



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
        fields = ('title', 'image')


class BlogListSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

