# Generated by Django 4.0 on 2022-01-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houston', '0003_alter_portfolio_load_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='originality',
            field=models.IntegerField(),
        ),
    ]