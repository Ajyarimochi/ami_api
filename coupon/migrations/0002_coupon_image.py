# Generated by Django 3.0.2 on 2020-01-03 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
