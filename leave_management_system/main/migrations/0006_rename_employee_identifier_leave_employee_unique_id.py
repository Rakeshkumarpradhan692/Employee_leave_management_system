# Generated by Django 5.0.4 on 2024-11-16 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_leave_applied_on_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leave',
            old_name='employee_identifier',
            new_name='employee_unique_id',
        ),
    ]
