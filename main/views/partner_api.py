from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from main.models import Partner, Product
from main.serializers import PartnerSerializer, ProductSerializer


class GetPartner(GenericAPIView):
    serializer_class = PartnerSerializer

    def get(self, request):
        partners = Partner.objects.all()
        serialized = self.get_serializer(partners, many=True)
        return Response(serialized.data)


class ProductByPartner(GenericAPIView):
    serializer_class = ProductSerializer

    def get(self, request, pk):
        products = Product.objects.filter(partner_id=pk)
        serialized = self.get_serializer(products, many=True)
        return Response(serialized.data)
