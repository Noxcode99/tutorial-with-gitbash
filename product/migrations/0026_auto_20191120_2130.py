# Generated by Django 2.2.3 on 2019-11-20 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_auto_20191120_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_alternate_cost',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_alternate_price',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sub_products',
            name='product_alternate_cost',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sub_products',
            name='product_alternate_price',
            field=models.CharField(max_length=10, null=True),
        ),
    ]