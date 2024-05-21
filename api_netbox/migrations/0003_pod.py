# Generated by Django 5.0.6 on 2024-05-21 13:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_netbox', '0002_netbox_created_at_netbox_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('netbox', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pods', to='api_netbox.netbox')),
            ],
        ),
    ]