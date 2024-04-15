# Generated by Django 5.0.2 on 2024-04-12 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auc_property',
            name='Property_Documents',
            field=models.FileField(blank=True, null=True, upload_to='property_documents'),
        ),
        migrations.AlterField(
            model_name='auc_property',
            name='Property_Pictures',
            field=models.ImageField(default=None, upload_to='pics'),
        ),
    ]
