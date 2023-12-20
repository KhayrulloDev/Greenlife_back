from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from main.serializers import FeedBackSerializer


class FeedbackGenericAPIView(GenericAPIView):
    serializer_class = FeedBackSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
