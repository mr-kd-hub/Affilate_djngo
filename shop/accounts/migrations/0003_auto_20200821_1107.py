# Generated by Django 3.0.8 on 2020-08-21 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200821_1105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelTable(
            name='customuser',
            table=None,
        ),
    ]