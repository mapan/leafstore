# Generated by Django 3.1.7 on 2021-03-19 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='slug',
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(editable=False, max_length=200),
        ),
    ]
