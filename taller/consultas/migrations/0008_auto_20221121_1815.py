# Generated by Django 2.2.2 on 2022-11-21 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0007_cambiarias_paisdestino'),
    ]

    operations = [
        migrations.AddField(
            model_name='cambiarias',
            name='valorTran_char',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AlterField(
            model_name='cambiarias',
            name='paisDestino',
            field=models.CharField(max_length=100),
        ),
    ]
