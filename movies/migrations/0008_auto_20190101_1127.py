# Generated by Django 2.1.1 on 2019-01-01 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_comment_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]
