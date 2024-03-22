# Generated by Django 5.0.2 on 2024-03-22 21:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_allproperty_property_documents'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='property_documents/', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
            ],
        ),
        migrations.RemoveField(
            model_name='allproperty',
            name='Property_Documents',
        ),
        migrations.AddField(
            model_name='allproperty',
            name='Property_Documents',
            field=models.ManyToManyField(related_name='properties', to='property.propertydocument'),
        ),
    ]