# Generated by Django 2.2.5 on 2019-09-18 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
