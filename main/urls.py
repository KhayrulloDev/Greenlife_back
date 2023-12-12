from django.urls import path

from .views import BlogAPIView, BlogDetailAPIView

urlpatterns = [
    path('blogs', BlogAPIView.as_view(), name='blogs'),
    path('blog-detail/<int:blog_id>', BlogDetailAPIView.as_view(), name='blog_detail'),
]
