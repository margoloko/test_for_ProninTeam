from django.apps import AppConfig


class DonationConfig(AppConfig):
    """Настройка приложения donation."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "donation"
    verbose_name = "Денежные сборы"
