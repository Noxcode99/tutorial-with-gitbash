# Generated by Django 2.2.3 on 2019-07-25 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20190718_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorisation',
            name='product_brand',
        ),
        migrations.AddField(
            model_name='categorisation',
            name='product_default_unit_prefix',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
