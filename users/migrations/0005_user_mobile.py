# Generated by Django 3.0 on 2020-01-28 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200123_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, max_length=150, verbose_name='Mobile nNumber'),
        ),
    ]
