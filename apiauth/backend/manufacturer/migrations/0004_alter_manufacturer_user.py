# Generated by Django 4.1 on 2023-03-26 00:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("manufacturer", "0003_alter_manufacturer_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="manufacturer",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="manufacturer",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
