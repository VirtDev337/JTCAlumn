# Generated by Django 4.0.3 on 2022-03-11 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_graduation_date_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='graduation_date_month',
            field=models.DateField(default=3),
        ),
        migrations.AlterField(
            model_name='profile',
            name='graduation_date_year',
            field=models.DateField(default=2022),
        ),
    ]
