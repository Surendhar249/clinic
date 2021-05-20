# Generated by Django 3.2 on 2021-05-20 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='age',
            field=models.PositiveIntegerField(default=18),
        ),
        migrations.AddField(
            model_name='details',
            name='heart_rate',
            field=models.FloatField(default=130),
        ),
        migrations.AddField(
            model_name='details',
            name='saturation_level',
            field=models.FloatField(default=80),
        ),
    ]