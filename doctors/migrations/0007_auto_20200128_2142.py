# Generated by Django 3.0 on 2020-01-28 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0006_auto_20200128_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='specialised',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='doctor_specialised', to='doctors.Specilaizations'),
        ),
    ]