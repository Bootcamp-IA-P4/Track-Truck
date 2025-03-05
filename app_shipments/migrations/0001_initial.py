# Generated by Django 5.1.6 on 2025-03-05 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('company_id', models.IntegerField()),
                ('driver_id', models.IntegerField(null=True)),
                ('description', models.TextField()),
                ('origin', models.TextField()),
                ('destination', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('finished_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'shipments',
            },
        ),
    ]
