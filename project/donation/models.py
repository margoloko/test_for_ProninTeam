from datetime import datetime as dt
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Event(models.TextChoices):
    """Модель для выбора повода сбора средств."""

    BIRTHDAY = "Birthday", "День рождения"
    WEDDING = "Wedding", "Свадьба"
    CHARITY = "Charity", "Благотворительность"
    TRAVEL = "Travel", "Путешествие"
    DATE = "Date", "Свидание"
    EDUCATION = "Education", "Оплата обучения или курсов"
    GIFT = "Gift", "Подарок"
    SPORTS_EVENT = "SportsEvent", "Спортивное соревнование"
    MEDICAL_TREATMENT = "MedicalTreatment", "Медицинское лечение"
    DISASTER_RECOVERY = "DisasterRecovery", "Восстановление после бедствия"
    OTHER = "Other", "Другое"


class Collect(models.Model):
    """Модель группового денежного сбора."""

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Автор сбора"
    )
    title = models.CharField(max_length=200, verbose_name="Название")
    occasion = models.CharField(
        max_length=50,
        choices=Event.choices,
        verbose_name="Повод",
        help_text="Выберите повод сбора",
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    goal = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Запланированная сумма"
    )
    current_sum = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name="Текущая сумма"
    )
    cover = models.ImageField(
        upload_to="media/covers/",
        blank=True,
        null=True,
        verbose_name="Обложка сбора",
        help_text="Добавьте картинку",
    )
    deadline = models.DateTimeField(
        default=dt.now() + timedelta(days=14), verbose_name="Дедлайн сбора"
    )
    timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Время и дата создания сбора"
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Денежный сбор"
        verbose_name_plural = "Денежные сборы"
        ordering = ["timestamp"]


class Payment(models.Model):
    """Модель платёжа для сбора."""

    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    collect = models.ForeignKey(
        Collect, on_delete=models.CASCADE, verbose_name="Денежный сбор"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Жертвователь"
    )
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Время платежа")

    def __str__(self) -> str:
        return f"{self.collect} - {self.amount}"

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = ["timestamp"]
