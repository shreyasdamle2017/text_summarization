# Generated by Django 3.0.5 on 2020-09-23 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0004_auto_20200921_1857'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='docfile',
            new_name='file',
        ),
    ]
