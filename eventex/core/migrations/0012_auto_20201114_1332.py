# Generated by Django 3.1.2 on 2020-11-14 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_delete_courseold'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='talk',
            options={'ordering': ['start'], 'verbose_name': 'palestra', 'verbose_name_plural': 'palestras'},
        ),
    ]