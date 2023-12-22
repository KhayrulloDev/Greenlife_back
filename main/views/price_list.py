from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from main.models import Product, Category
from main.serializers import ProductPriceListSerializer


class PriceListGenericAPIView(GenericAPIView):
    serializer_class = ProductPriceListSerializer

    def get(self, request):
        categories = Category.objects.all()
        list_data = []
        for category in categories:
            products = Product.objects.filter(category_id=category.id)
            serializer = self.get_serializer(products, many=True)
            product_dict = {
                category.name: serializer.data
            }
            list_data.append(product_dict)

        return Response(list_data)
