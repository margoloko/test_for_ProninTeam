from django.contrib import admin

from .models import Collect, Payment


@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    """Админка для модели Collect."""

    pass


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """Админка для модели Payment."""

    pass
