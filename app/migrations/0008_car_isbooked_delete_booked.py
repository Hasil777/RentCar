# Generated by Django 4.2.4 on 2024-08-27 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='isbooked',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.DeleteModel(
            name='Booked',
        ),
    ]
