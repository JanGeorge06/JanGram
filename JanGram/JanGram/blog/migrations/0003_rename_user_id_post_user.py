# Generated by Django 5.0 on 2023-12-20 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_user_post_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='user_id',
            new_name='user',
        ),
    ]