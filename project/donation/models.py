from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Event(models.TextChoices):
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

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    occasion = models.CharField(max_length=50, choices=Event.choices)
    description = models.TextField()
    goal = models.DecimalField(max_digits=10, decimal_places=2)
    current_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    contributors = models.IntegerField()
    cover = models.ImageField(upload_to="media/covers/")
    deadline = models.DateTimeField()


class Payment(models.Model):
    """Модель платёжа для сбора."""

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    collect = models.ForeignKey(Collect, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
