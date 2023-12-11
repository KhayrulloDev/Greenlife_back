from rest_framework.serializers import ModelSerializer

from .models import Partner


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'

