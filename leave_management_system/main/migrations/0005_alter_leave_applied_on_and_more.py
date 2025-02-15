# Generated by Django 5.0.4 on 2024-11-16 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_leave_employee_identifier_alter_leave_leave_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='applied_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='employee_identifier',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='leave',
            name='leave_type',
            field=models.CharField(choices=[('Sick', 'Sick Leave'), ('Casual', 'Casual Leave'), ('Earned', 'Earned Leave'), ('Maternity', 'Maternity Leave'), ('Paternity', 'Paternity Leave'), ('Vacation', 'Vacation Leave')], max_length=20),
        ),
    ]
