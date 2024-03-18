from django.contrib import admin

from .models import Collect, Payment


@admin.register(Collect)
class CollectAdmin(admin.ModelAdmin):
    """Админка для модели Collect."""

    list_display = ("title", "author", "occasion", "current_sum", "goal", "deadline")
    list_filter = ("title", "author", "occasion", "goal", "deadline", "timestamp")
    search_fields = ("title", "author", "occasion", "goal", "deadline")
    ordering = (
        "title",
        "author",
        "occasion",
        "current_sum",
        "timestamp",
        "goal",
        "deadline",
    )
    readonly_fields = "timestamp"
    empty_value_display = "-пусто-"


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    """Админка для модели Payment."""

    list_display = ("user", "amount", "collect")
    list_filter = ("user", "amount", "collect", "timestamp")
    search_fields = ("user", "amount", "collect", "timestamp")
    ordering = ("user", "amount", "collect", "timestamp")
    readonly_fields = "timestamp"
    empty_value_display = "-пусто-"
