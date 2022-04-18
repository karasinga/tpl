# Generated by Django 3.2.5 on 2022-04-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_twinkle'),
    ]

    operations = [
        migrations.AddField(
            model_name='twinkle',
            name='year',
            field=models.IntegerField(choices=[(2020, 2020), (2021, 2021), (2022, 2022)], default=2022, null=True),
        ),
    ]
