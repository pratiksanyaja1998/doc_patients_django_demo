# Generated by Django 3.0 on 2020-01-28 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_specilaizations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='specialised',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='doctor_specialised', to='doctors.Specilaizations'),
        ),
    ]