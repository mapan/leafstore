# Generated by Django 3.1.7 on 2021-03-29 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210326_0914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcolor',
            name='stock',
            field=models.IntegerField(default=1),
        ),
    ]
