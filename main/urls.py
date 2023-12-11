from django.urls import path

from .views import GetPartner, ProductByPartner

urlpatterns = [
    path('get-partners', GetPartner.as_view(), name='partners'),
    path('partner/<int:pk>/product', ProductByPartner.as_view(), name='partner-products'),
]
