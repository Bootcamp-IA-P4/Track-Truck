# Generated by Django 5.1.6 on 2025-02-26 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
                'db_table': 'companies',
                'managed': False,
            },
        ),
    ]
