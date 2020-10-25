# Generated by Django 2.2.16 on 2020-10-25 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=128)),
                ('product_detail', models.TextField()),
                ('product_barcode', models.CharField(max_length=32)),
                ('product_qty', models.IntegerField()),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('product_image', models.CharField(max_length=64)),
                ('product_status', models.IntegerField()),
            ],
        ),
    ]
