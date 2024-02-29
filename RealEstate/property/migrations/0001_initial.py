# Generated by Django 5.0.2 on 2024-02-29 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.TextField(default=None)),
                ('Price', models.IntegerField(default=0)),
                ('Media', models.ImageField(upload_to='pics')),
                ('Road_No', models.CharField(max_length=4)),
                ('Block', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=4)),
                ('District', models.CharField(max_length=100)),
                ('Rent', models.BooleanField(default=False)),
                ('Sale', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('commercial', 'Commercial'), ('land', 'Land'), ('residential', 'Residential')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='CommercialProperty',
            fields=[
                ('allproperty_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='property.allproperty')),
                ('House_No', models.CharField(max_length=8)),
                ('business_type', models.CharField(max_length=100)),
                ('total_area', models.DecimalField(decimal_places=2, max_digits=8)),
                ('parking_spaces', models.PositiveIntegerField(default=0)),
                ('has_elevator', models.BooleanField(default=False)),
                ('has_security_system', models.BooleanField(default=False)),
                ('has_conference_room', models.BooleanField(default=False)),
                ('year_built', models.DateTimeField(blank=True, null=True)),
            ],
            bases=('property.allproperty',),
        ),
        migrations.CreateModel(
            name='LandProperty',
            fields=[
                ('allproperty_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='property.allproperty')),
                ('land_area', models.DecimalField(decimal_places=2, max_digits=8)),
                ('land_type', models.CharField(max_length=100)),
                ('road_access', models.BooleanField(default=True)),
                ('is_fenced', models.BooleanField(default=False)),
            ],
            bases=('property.allproperty',),
        ),
        migrations.CreateModel(
            name='ResidentialProperty',
            fields=[
                ('allproperty_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='property.allproperty')),
                ('House_No', models.CharField(max_length=8)),
                ('floor_count', models.PositiveIntegerField(default=1)),
                ('bedroom_count', models.PositiveIntegerField(default=1)),
                ('bathroom_count', models.PositiveIntegerField(default=1)),
                ('garage_spaces', models.PositiveIntegerField(default=0)),
                ('has_pool', models.BooleanField(default=False)),
                ('has_garden', models.BooleanField(default=False)),
                ('has_balcony', models.BooleanField(default=False)),
                ('year_built', models.DateTimeField(blank=True, null=True)),
            ],
            bases=('property.allproperty',),
        ),
    ]
