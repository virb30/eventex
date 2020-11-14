# Generated by Django 3.1.2 on 2020-11-14 16:32

from django.db import migrations
import hashid_field.field


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_auto_20201104_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='id',
            field=hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, primary_key=True, serialize=False),
        ),
    ]
