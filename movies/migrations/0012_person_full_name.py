# Generated by Django 2.1.1 on 2019-01-04 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20190103_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='full_name',
            field=models.CharField(default='', max_length=60),
        ),
    ]