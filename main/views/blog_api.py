from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response

from main.models import Blog
from main.serializers import BlogSerializer, BlogListSerializer


class BlogAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = ()


class BlogDetailAPIView(GenericAPIView):
    permission_classes = ()
    serializer_class = BlogListSerializer

    def get(self, request, blog_id):
        blogs = Blog.objects.filter(id=blog_id)
        serializer_blog = self.get_serializer(blogs, many=True)
        return Response(serializer_blog.data)
