# Generated by Django 5.0.6 on 2024-05-17 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kirrurl',
            name='shortcode',
            field=models.CharField(default='cfedefaultshortcode', max_length=15),
            preserve_default=False,
        ),
    ]
