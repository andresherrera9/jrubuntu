# Generated by Django 2.2.2 on 2022-09-26 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0003_auto_20220926_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='efectivo',
            name='TransaccionValor',
            field=models.CharField(max_length=50),
        ),
    ]
