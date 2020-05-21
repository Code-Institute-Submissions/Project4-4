# Generated by Django 2.2.6 on 2020-05-21 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0008_auto_20200521_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendordeliverypostal',
            name='postal_code',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='vendordeliverytown',
            name='town',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]