# Generated by Django 3.2.3 on 2021-08-24 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_stuff_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='created',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
    ]
