# Generated by Django 2.2.6 on 2020-05-21 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0007_auto_20200521_0737'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='vendordeliverypostal',
            field=models.ManyToManyField(to='vendor.VendorDeliveryPostal'),
        ),
        migrations.AddField(
            model_name='vendor',
            name='vendordeliverytown',
            field=models.ManyToManyField(to='vendor.VendorDeliveryTown'),
        ),
    ]