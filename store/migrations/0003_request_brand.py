# Generated by Django 4.2.7 on 2024-01-16 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='brand',
            field=models.CharField(default=0, max_length=100),
        ),
    ]