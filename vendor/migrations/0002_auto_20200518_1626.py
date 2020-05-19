# Generated by Django 2.2.6 on 2020-05-18 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='owner_contact',
            new_name='user_contact',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='owner_email',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='owner_name',
        ),
        migrations.AddField(
            model_name='vendor',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]