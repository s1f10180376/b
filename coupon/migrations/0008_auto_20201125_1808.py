# Generated by Django 2.1.2 on 2020-11-25 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0007_auto_20201125_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='term',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coupon.Shop'),
        ),
    ]
