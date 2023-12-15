from django.urls import path
from .views import GetPartner, ProductByPartner
from .views.categories import CategoryGenericAPIView, CategoryParentGenericAPIView
from .views.feedbacks import FeedbackGenericAPIView
from .views.price_list import PriceListGenericAPIView
from .views.products import ProductWithCategoryGenericAPIView, OrderProductGenericAPIView, ProductGenericAPIView

urlpatterns = [
    path('parent-categories', CategoryParentGenericAPIView.as_view(), name='parent_categories'),
    path('categories/<int:parent_id>', CategoryGenericAPIView.as_view(), name='categories'),
    path('price-list', PriceListGenericAPIView.as_view(), name='price_list'),
    path('product-list/<int:pk>', ProductGenericAPIView.as_view(), name='product_list'),
    path('products/<int:category_id>', ProductWithCategoryGenericAPIView.as_view(), name='products'),
    path('order-product', OrderProductGenericAPIView.as_view(), name='order_product'),
    path('get-partners', GetPartner.as_view(), name='partners'),
    path('partner/<int:pk>/product', ProductByPartner.as_view(), name='partner-products'),
    path('feedback', FeedbackGenericAPIView.as_view(), name='feedback'),
]
