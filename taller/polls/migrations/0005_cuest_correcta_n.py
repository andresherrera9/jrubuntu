# Generated by Django 2.2.2 on 2022-09-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_remove_answ_correct_n'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuest',
            name='correcta_n',
            field=models.IntegerField(default=0),
        ),
    ]