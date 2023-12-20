
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from main.models import Order
from main.serializers import OrderProductSerializer


class OrderProductGenericAPIView(GenericAPIView):
    serializer_class = OrderProductSerializer

    def get(self, request):

        data = Order.objects.filter(status=0)
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as e:
            return Response({"message": str(e)}, status=404)
        return Response(serializer.data)


class OrderPatchView(GenericAPIView):
    serializer_class = Order

    def patch(self, request, pk):
        order = Order.objects.get(pk=pk)
        serializer = self.get_serializer(order, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
