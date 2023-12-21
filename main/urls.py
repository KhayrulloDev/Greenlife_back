from django.urls import path
from .views import GetPartner, ProductByPartner
from .views.blogs import BlogListGenericAPIView, BlogDetailGenericAPIView
from .views.categories import CategoryGenericAPIView, CategoryParentGenericAPIView
from .views.feedbacks import FeedbackGenericAPIView
from .views.price_list import PriceListGenericAPIView
from .views.products import ProductWithCategoryGenericAPIView, OrderProductGenericAPIView, ProductGenericAPIView
from .views.reviews import ReviewGenericAPIView

urlpatterns = [
    path('parent-categories', CategoryParentGenericAPIView.as_view(), name='parent_categories'),
    path('categories/<int:parent_id>', CategoryGenericAPIView.as_view(), name='categories'),
    path('price-list', PriceListGenericAPIView.as_view(), name='price_list'),
    path('product-detail/<int:pk>', ProductGenericAPIView.as_view(), name='product_detail'),
    path('products/<int:category_id>', ProductWithCategoryGenericAPIView.as_view(), name='products'),
    path('order-product', OrderProductGenericAPIView.as_view(), name='order_product'),
    path('blog-list', BlogListGenericAPIView.as_view(), name='blog_list'),
    path('blog-detail<int:pk>', BlogDetailGenericAPIView.as_view(), name='blog_detail'),
    path('get-partners', GetPartner.as_view(), name='partners'),
    path('partnerproduct<int:pk>', ProductByPartner.as_view(), name='partner-products'),
    path('feedback', FeedbackGenericAPIView.as_view(), name='feedback'),
    path('review', ReviewGenericAPIView.as_view(), name='review'),
]
