# Generated by Django 4.0.4 on 2022-05-15 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_otp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otp',
            old_name='is_verifyed',
            new_name='is_verified',
        ),
    ]
