# Generated by Django 3.2 on 2021-05-20 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_auto_20210520_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='sex',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'other')], default='male', max_length=6),
        ),
    ]