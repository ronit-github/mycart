# Generated by Django 3.2.4 on 2021-07-14 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='ctitle',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
