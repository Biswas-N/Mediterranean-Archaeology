# Generated by Django 2.1.2 on 2018-10-31 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homePage', '0002_auto_20181031_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordimage',
            name='image_count',
        ),
        migrations.AddField(
            model_name='record',
            name='image_count',
            field=models.IntegerField(null=True),
        ),
    ]
