# Generated by Django 5.0.6 on 2024-05-21 15:11

import shortener.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_alter_kirrurl_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kirrurl',
            name='url',
            field=models.CharField(max_length=220, validators=[shortener.validators.validate_url, shortener.validators.validate_dot_com]),
        ),
    ]
