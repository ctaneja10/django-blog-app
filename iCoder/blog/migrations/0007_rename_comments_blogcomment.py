# Generated by Django 4.0.6 on 2022-08-05 04:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='BlogComment',
        ),
    ]