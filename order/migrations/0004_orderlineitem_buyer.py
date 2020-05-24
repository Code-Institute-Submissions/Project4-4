# Generated by Django 2.2.6 on 2020-05-24 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0005_auto_20200521_0953'),
        ('order', '0003_delete_order_line_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='buyer.Buyer'),
        ),
    ]
