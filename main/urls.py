from django.urls import path
from .views import GetPartner, ProductByPartner, BlogAPIView, BlogDetailAPIView
from .views import GetPartner, ProductByPartner
from .views.feedbacks import FeedbackGenericAPIView
from .views.price_list import PriceListGenericAPIView
from .views.products import ProductWithCategoryGenericAPIView, OrderProductGenericAPIView, ProductGenericAPIView

urlpatterns = [
    path('price-list', PriceListGenericAPIView.as_view(), name='price_list'),
    path('products-list/<int:pk>', ProductGenericAPIView.as_view(), name='product_data'),
    path('products/<int:category_id>', ProductWithCategoryGenericAPIView.as_view(), name='products'),
    path('order-product', OrderProductGenericAPIView.as_view(), name='order_product'),
    path('get-partners', GetPartner.as_view(), name='partners'),
    path('partner/<int:pk>/product', ProductByPartner.as_view(), name='partner-products'),
    path('blogs', BlogAPIView.as_view(), name='blogs'),
    path('blog-detail/<int:blog_id>', BlogDetailAPIView.as_view(), name='blog_detail'),
    path('feedback', FeedbackGenericAPIView.as_view(), name='feedback'),
]
