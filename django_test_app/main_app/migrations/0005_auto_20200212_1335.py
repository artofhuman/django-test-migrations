# Generated by Django 2.2.8 on 2020-02-12 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20191119_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='someitem',
            name='amount',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=19),
        ),
    ]