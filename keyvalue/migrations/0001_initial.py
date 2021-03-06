# Generated by Django 3.2.3 on 2021-05-23 18:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeUUID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_date', models.DateTimeField(auto_now_add=True)),
                ('uuid_value', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
        ),
    ]
