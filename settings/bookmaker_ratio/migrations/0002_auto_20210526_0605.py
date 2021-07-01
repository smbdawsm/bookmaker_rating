# Generated by Django 3.2.3 on 2021-05-26 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmaker_ratio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmaker',
            name='bonus',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Bonus'),
        ),
        migrations.AddField(
            model_name='bookmaker',
            name='name',
            field=models.CharField(default=None, max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='bookmaker',
            name='description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='bookmaker',
            name='url',
            field=models.CharField(default=None, max_length=255, verbose_name='URL'),
        ),
    ]