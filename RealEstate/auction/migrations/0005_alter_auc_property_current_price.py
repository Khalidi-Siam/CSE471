# Generated by Django 5.0.2 on 2024-03-30 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_alter_auc_property_current_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auc_property',
            name='current_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
