# Generated by Django 3.2.5 on 2021-08-10 22:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_review_date_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='product',
            new_name='product_id',
        ),
        migrations.AlterField(
            model_name='review',
            name='date_review',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 10, 18, 36, 15, 525032)),
        ),
    ]
