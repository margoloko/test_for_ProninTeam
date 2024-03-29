from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from .models import Collect, Payment

User = get_user_model()


class PaymentSerializer(ModelSerializer):
    """."""

    class Meta:
        model = Payment
        fields = ("id", "user", "amount", "collect", "timestamp")


class CollectSerializer(ModelSerializer):
    """."""

    class Meta:
        model = Collect
        fields = ("id",)
