# Generated by Django 3.2.5 on 2022-04-17 08:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sales',
            name='month',
            field=models.CharField(choices=[('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], default=4, max_length=9),
        ),
    ]
