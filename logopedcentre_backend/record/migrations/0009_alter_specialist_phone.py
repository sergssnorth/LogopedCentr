# Generated by Django 4.2.7 on 2023-12-13 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0008_remove_specialist_thumbnail_specialist_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialist',
            name='phone',
            field=models.CharField(max_length=255),
        ),
    ]
