# Generated by Django 5.0.6 on 2024-05-17 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_kirrurl_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
