# Generated by Django 5.1.6 on 2025-02-26 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user_type', models.CharField(choices=[('company', 'Company'), ('driver', 'Driver')], max_length=10)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
