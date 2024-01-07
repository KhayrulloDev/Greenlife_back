from django.urls import path
from .views import GetPartner, ProductByPartner
from .views.blogs import BlogListGenericAPIView, BlogDetailGenericAPIView
from .views.categories import CategoryGenericAPIView, CategoryParentGenericAPIView
from .views.products import ProductWithCategoryGenericAPIView, OrderProductGenericAPIView, ProductGenericAPIView


urlpatterns = [
    path('parent-categories', CategoryParentGenericAPIView.as_view(), name='parent_categories'),
    path('categories/<int:parent_id>', CategoryGenericAPIView.as_view(), name='categories'),
    path('product-detail/<int:pk>', ProductGenericAPIView.as_view(), name='product_detail'),
    path('products/<int:category_id>', ProductWithCategoryGenericAPIView.as_view(), name='products'),
    path('order-product', OrderProductGenericAPIView.as_view(), name='order_product'),
    path('blog-list', BlogListGenericAPIView.as_view(), name='blog_list'),
    path('blog-detail<int:pk>', BlogDetailGenericAPIView.as_view(), name='blog_detail'),
    path('get-partners', GetPartner.as_view(), name='partners'),
    path('partnerproduct<int:pk>', ProductByPartner.as_view(), name='partner-products'),
]
