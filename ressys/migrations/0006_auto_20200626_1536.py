# Generated by Django 3.0.3 on 2020-06-26 20:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ressys', '0005_auto_20200625_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
