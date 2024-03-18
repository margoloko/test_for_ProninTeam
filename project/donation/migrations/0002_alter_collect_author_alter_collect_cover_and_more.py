# Generated by Django 5.0.2 on 2024-03-18 11:23

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("donation", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="collect",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор сбора",
            ),
        ),
        migrations.AlterField(
            model_name="collect",
            name="cover",
            field=models.ImageField(
                blank=True,
                help_text="Добавьте картинку",
                null=True,
                upload_to="media/covers/",
                verbose_name="Обложка сбора",
            ),
        ),
        migrations.AlterField(
            model_name="collect",
            name="current_sum",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10, verbose_name="Текущая сумма"
            ),
        ),
        migrations.AlterField(
            model_name="collect",
            name="deadline",
            field=models.DateTimeField(
                default=datetime.datetime(2024, 4, 1, 18, 23, 25, 141533),
                verbose_name="Дедлайн сбора",
            ),
        ),
        migrations.AlterField(
            model_name="collect",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="collect",
            name="goal",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Запланированная сумма"
            ),
        ),
        migrations.AlterField(
            model_name="collect",
            name="occasion",
            field=models.CharField(
                choices=[
                    ("Birthday", "День рождения"),
                    ("Wedding", "Свадьба"),
                    ("Charity", "Благотворительность"),
                    ("Travel", "Путешествие"),
                    ("Date", "Свидание"),
                    ("Education", "Оплата обучения или курсов"),
                    ("Gift", "Подарок"),
                    ("SportsEvent", "Спортивное соревнование"),
                    ("MedicalTreatment", "Медицинское лечение"),
                    ("DisasterRecovery", "Восстановление после бедствия"),
                    ("Other", "Другое"),
                ],
                help_text="Выберите повод сбора",
                max_length=50,
                verbose_name="Повод",
            ),
        ),
        migrations.AlterField(
            model_name="collect",
            name="timestamp",
            field=models.DateTimeField(
                auto_now_add=True, verbose_name="Время и дата создания сбора"
            ),
        ),
        migrations.AlterField(
            model_name="collect",
            name="title",
            field=models.CharField(max_length=200, verbose_name="Название"),
        ),
        migrations.AlterField(
            model_name="payment",
            name="amount",
            field=models.DecimalField(
                decimal_places=2, max_digits=10, verbose_name="Сумма"
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="collect",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="donation.collect",
                verbose_name="Денежный сбор",
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Время платежа"),
        ),
        migrations.AlterField(
            model_name="payment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Жертвователь",
            ),
        ),
    ]