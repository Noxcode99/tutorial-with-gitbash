# Generated by Django 2.2.3 on 2019-10-21 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0014_reports'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='invoice_no',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
