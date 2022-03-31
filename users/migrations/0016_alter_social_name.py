# Generated by Django 4.0.3 on 2022-03-24 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_social_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='name',
            field=models.CharField(blank=True, choices=[('github', 'Github'), ('linkedin', 'LinkedIn'), ('twitter', 'Twitter'), ('youtube', 'YouTube'), ('facebook', 'Facebook'), ('website', 'Website')], default='github', max_length=200, null=True),
        ),
    ]
