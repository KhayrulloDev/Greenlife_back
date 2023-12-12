from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from main.serializers import ReviewSerializer


class ReviewGenericAPIView(GenericAPIView):
    serializer_class = ReviewSerializer

    def post(self, request):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as e:
            return Response({"message": str(e)}, status=404)
        return Response(serializer.data)

