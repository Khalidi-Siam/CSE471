# Generated by Django 5.0.2 on 2024-03-20 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_userprofile_profile_picture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
    ]