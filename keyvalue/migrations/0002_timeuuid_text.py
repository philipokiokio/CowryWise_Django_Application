# Generated by Django 3.2.3 on 2021-05-23 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keyvalue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeuuid',
            name='text',
            field=models.CharField(default=0, max_length=2),
            preserve_default=False,
        ),
    ]