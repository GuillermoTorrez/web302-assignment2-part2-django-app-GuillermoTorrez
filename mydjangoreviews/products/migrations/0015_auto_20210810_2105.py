# Generated by Django 3.2.5 on 2021-08-11 01:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_review_date_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_review',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 10, 21, 5, 39, 37079)),
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(choices=[(5, 'Excelent'), (4, 'Good'), (3, 'Fair'), (2, 'Poor'), (1, 'Very Poor')]),
        ),
    ]
