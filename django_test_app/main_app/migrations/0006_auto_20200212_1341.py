# Generated by Django 2.2.8 on 2020-02-12 13:41

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20200212_1335'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='someitem',
            constraint=models.CheckConstraint(check=models.Q(amount__gt=0), name='check_amount'),
        ),
    ]
