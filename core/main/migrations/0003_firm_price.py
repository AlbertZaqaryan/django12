# Generated by Django 4.0.4 on 2022-06-04 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='firm',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Firm price'),
        ),
    ]
