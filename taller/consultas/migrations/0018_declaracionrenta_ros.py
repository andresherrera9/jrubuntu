# Generated by Django 2.2.2 on 2023-11-15 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0017_auto_20231031_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='declaracionrenta',
            name='ros',
            field=models.IntegerField(default=0),
        ),
    ]