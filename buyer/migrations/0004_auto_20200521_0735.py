# Generated by Django 2.2.6 on 2020-05-21 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0003_auto_20200521_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='postal_code',
            field=models.PositiveIntegerField(),
        ),
    ]