# Generated by Django 3.2.3 on 2021-12-24 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20211224_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='your_text',
            field=models.TextField(blank=True),
        ),
    ]