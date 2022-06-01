# Generated by Django 4.0.4 on 2022-05-24 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='static/images/product')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_phone', models.CharField(max_length=100)),
                ('customer_address', models.CharField(max_length=100)),
                ('qty', models.IntegerField()),
                ('price_unit', models.IntegerField()),
                ('total', models.IntegerField()),
                ('order_date', models.DateTimeField()),
                ('deliver_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.product')),
            ],
        ),
    ]