# Generated by Django 3.2.5 on 2021-08-11 00:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_review_date_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_review',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 10, 20, 38, 24, 436347)),
        ),
    ]