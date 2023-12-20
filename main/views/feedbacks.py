from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from main.models.feedback import Feedback
from main.serializers import FeedBackSerializer, FeedBackSerializerForPatch


class FeedbackGenericAPIView(GenericAPIView):
    serializer_class = FeedBackSerializer

    def get(self, request):
        data = Feedback.objects.filter(status=0)
        serializer = self.get_serializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class FeedbackCheckedView(GenericAPIView):
    serializer_class = FeedBackSerializerForPatch

    def patch(self, request, pk):
        feedback = Feedback.objects.get(pk=pk)
        serializer = self.get_serializer(feedback, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


