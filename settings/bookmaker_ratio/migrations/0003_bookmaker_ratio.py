# Generated by Django 3.2.3 on 2021-05-26 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmaker_ratio', '0002_auto_20210526_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmaker',
            name='ratio',
            field=models.IntegerField(default=0, verbose_name='Rating'),
        ),
    ]
