# Generated by Django 5.0.6 on 2024-06-29 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_delete_facility'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
