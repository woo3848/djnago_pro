# Generated by Django 2.1.15 on 2020-10-27 06:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_member_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='phonenum',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
