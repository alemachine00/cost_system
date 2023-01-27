# Generated by Django 4.1.5 on 2023-01-25 15:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=10)),
                ('order_date', models.DateField(default=datetime.datetime(2023, 1, 1, 0, 0))),
                ('amount', models.IntegerField(default=0)),
                ('unit', models.CharField(max_length=5)),
                ('order_finished', models.BooleanField(default=False, help_text='Is this order finished?')),
            ],
            options={
                'ordering': ['-order_date'],
            },
        ),
        migrations.CreateModel(
            name='WorkTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=10)),
                ('employee_last_name', models.CharField(max_length=10)),
                ('date', models.DateField(default=datetime.datetime(2023, 1, 1, 0, 0))),
                ('entry_time', models.TimeField(default=datetime.datetime(2022, 1, 24, 6, 0))),
                ('finish_time', models.TimeField(default=datetime.datetime(2022, 1, 24, 12, 0))),
                ('hourly_rate', models.FloatField(default=0)),
                ('order_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cost.order')),
            ],
        ),
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=10)),
                ('amount', models.IntegerField(default=0)),
                ('unit', models.CharField(max_length=5)),
                ('unity_cost', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.datetime(2023, 1, 1, 0, 0))),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cost.order')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]