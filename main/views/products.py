from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from main.models import Product
from main.serializers import ProductSerializer, OrderProductSerializer, ProductWithCategory


class ProductWithCategoryGenericAPIView(GenericAPIView):
    serializer_class = ProductWithCategory

    def get(self, request, category_id):
        try:
            products = Product.objects.filter(category_id=category_id)
            serializer = self.get_serializer(products, many=True)
        except Exception as e:
            return Response({"message": str(e)}, status=404)
        return Response(serializer.data)


class ProductGenericAPIView(GenericAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Product.objects.filter(partner_id=pk)

    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            serializer = self.get_serializer(product)
        except Exception as e:
            return Response({"message": str(e)}, status=404)
        return Response(serializer.data)


class OrderProductGenericAPIView(GenericAPIView):
    serializer_class = OrderProductSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

