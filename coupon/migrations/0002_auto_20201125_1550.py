# Generated by Django 2.1.2 on 2020-11-25 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='term',
            field=models.IntegerField(default=6),
        ),
    ]
