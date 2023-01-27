# Generated by Django 4.1.5 on 2023-01-26 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost', '0003_alter_order_amount_alter_order_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workticket',
            name='work_hours',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='requisition',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='description',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='unity_cost',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='workticket',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='workticket',
            name='entry_time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='workticket',
            name='finish_time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='workticket',
            name='hourly_rate',
            field=models.FloatField(),
        ),
    ]