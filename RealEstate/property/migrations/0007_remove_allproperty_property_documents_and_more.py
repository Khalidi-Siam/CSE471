# Generated by Django 5.0.2 on 2024-03-22 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_propertydocument_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allproperty',
            name='Property_Documents',
        ),
        migrations.DeleteModel(
            name='PropertyDocument',
        ),
        migrations.AddField(
            model_name='allproperty',
            name='Property_Documents',
            field=models.FileField(blank=True, null=True, upload_to='property_documents'),
        ),
    ]
