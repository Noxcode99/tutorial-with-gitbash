# Generated by Django 2.2.3 on 2019-08-17 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20190814_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_price',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='sub_products',
            name='product_price',
            field=models.CharField(max_length=50),
        ),
    ]
