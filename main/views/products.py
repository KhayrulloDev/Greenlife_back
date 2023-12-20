from rest_framework.generics import GenericAPIView, RetrieveAPIView
from rest_framework.response import Response
from main.models import Product, File
from main.serializers import ProductSerializer, OrderProductSerializer, ProductWithCategory


class ProductWithCategoryGenericAPIView(GenericAPIView):
    serializer_class = ProductWithCategory

    def get(self, request, category_id):
        try:
            products = Product.objects.filter(category_id=category_id)
            serializer = self.get_serializer(products, many=True)
            list_data = []
            for product in serializer.data:
                product['image'] = File.objects.get(product_id=product['id']).file.url
                list_data.append(product)
        except Exception as e:
            return Response({"message": str(e)}, status=404)
        return Response(list_data)


class ProductGenericAPIView(GenericAPIView):
    serializer_class = ProductSerializer

    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = self.get_serializer(product)
            image = File.objects.get(product_id=product.id).file.url
            serialized_data = serializer.data
            serialized_data['image'] = image
            return Response(serialized_data)
        except Product.DoesNotExist:
            return Response({"message": "Product not found!"}, status=404)
        except Exception as e:
            return Response({"message": str(e)}, status=500)


class OrderProductGenericAPIView(GenericAPIView):
    serializer_class = OrderProductSerializer

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as e:
            return Response({"message": str(e)}, status=404)
        return Response(serializer.data)

