# Generated by Django 4.2.11 on 2024-07-01 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitob',
            name='more_info',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]
