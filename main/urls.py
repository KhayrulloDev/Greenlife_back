from django.urls import path


from .views import GetPartner, ProductByPartner, BlogAPIView, BlogDetailAPIView

urlpatterns = [
    path('get-partners', GetPartner.as_view(), name='partners'),
    path('partner/<int:pk>/product', ProductByPartner.as_view(), name='partner-products'),
    path('blogs', BlogAPIView.as_view(), name='blogs'),
    path('blog-detail/<int:blog_id>', BlogDetailAPIView.as_view(), name='blog_detail'),

]
