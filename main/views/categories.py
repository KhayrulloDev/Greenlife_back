from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from main.models import Category
from main.serializers import CategorySerializer


class CategoryGenericAPIView(GenericAPIView):
    serializer_class = CategorySerializer

    def get(self, request, parent_id):
        try:
            categories = Category.objects.filter(parent_id=parent_id)
            serializer = self.get_serializer(categories, many=True)
        except Exception as e:
            return Response({"message": str(e)}, status=404)
        return Response(serializer.data)


class CategoryParentGenericAPIView(GenericAPIView):
    serializer_class = CategorySerializer

    def get(self, request):
        try:
            categories = Category.objects.filter(parent_id=None)
            serializer = self.get_serializer(categories, many=True)
        except Exception as e:
            return Response({"message": str(e)}, status=404)
        return Response(serializer.data)
