# Generated by Django 3.0.4 on 2020-07-09 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20200709_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentorcourse',
            old_name='Mentor',
            new_name='mentor',
        ),
    ]