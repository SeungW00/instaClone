# Generated by Django 2.0.8 on 2018-09-27 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20180917_0304'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]