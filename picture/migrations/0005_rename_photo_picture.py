# Generated by Django 5.0.7 on 2024-08-17 16:12

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picture', '0004_alter_photo_category_alter_photo_created_by'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photo',
            new_name='Picture',
        ),
    ]
