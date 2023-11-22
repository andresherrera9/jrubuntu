# Generated by Django 2.2.2 on 2022-11-21 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0005_remove_efectivo_transaccionvalor'),
    ]

    operations = [
        migrations.AddField(
            model_name='declaracionrenta',
            name='gastos_char',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='declaracionrenta',
            name='ingresoBruto_char',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='declaracionrenta',
            name='ingresoLiquido_char',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='declaracionrenta',
            name='pasivo_char',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='declaracionrenta',
            name='patrimonioBruto_char',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='declaracionrenta',
            name='patrimonioLiquido_char',
            field=models.CharField(default=0, max_length=200),
        ),
    ]