# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 18:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', help_text='Letters only, max length = 20', max_length=20)),
                ('lastname', models.CharField(default='', help_text='Letters only, max length = 30', max_length=30)),
                ('username', models.CharField(default='', help_text='Only letters, numbers, underscores or hyphens, max length = 20', max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40)),
                ('phone', models.CharField(blank=True, default='', help_text='+375xxxxxxxxx', max_length=13)),
                ('addresslist', models.CommaSeparatedIntegerField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newsheader', models.CharField(max_length=50)),
                ('newstext', models.TextField(default='')),
                ('newsdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderstartdate', models.DateTimeField(auto_now_add=True)),
                ('orderenddate', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Done', 'Done'), ('Canceled', 'Canceled')], default='Open', max_length=14)),
                ('ordercost', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=8)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Client')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(default='none', help_text='Use the following format: image002.jpg or gitars/gitara042.png', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('manufacturer', models.CharField(blank=True, default='', max_length=40)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('photo', models.CommaSeparatedIntegerField(blank=True, max_length=500)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.SubCategory'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product'),
        ),
    ]
