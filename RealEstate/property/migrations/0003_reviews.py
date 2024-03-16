# Generated by Django 5.0.2 on 2024-03-16 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_userprofile_profile_picture_and_more'),
        ('property', '0002_alter_commercialproperty_business_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1000)),
                ('rating', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.allproperty')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.userprofile')),
            ],
            options={
                'unique_together': {('property', 'user')},
            },
        ),
    ]