# Generated by Django 4.0.5 on 2022-07-12 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kingcounty', '0002_alter_data_options_data_crime_count_normalized_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='crime_count_normalized',
            field=models.FloatField(default=0),
        ),
    ]