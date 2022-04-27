# Generated by Django 2.2.2 on 2019-06-28 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_taxes_price_tax_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_sales_final',
            name='sales_cash_account',
            field=models.CharField(choices=[('General', 'General'), ('General', 'General'), ('General', 'General')], max_length=8),
        ),
        migrations.AlterField(
            model_name='create_sales_final',
            name='sales_transaction_mode',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Bank', 'Bank')], max_length=5),
        ),
    ]