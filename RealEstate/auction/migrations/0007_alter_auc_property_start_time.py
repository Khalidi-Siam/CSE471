# Generated by Django 5.0.2 on 2024-04-17 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0006_merge_20240415_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auc_property',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]