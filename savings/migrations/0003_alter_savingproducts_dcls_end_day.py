# Generated by Django 4.2.16 on 2024-11-19 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savings', '0002_alter_savingproducts_max_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savingproducts',
            name='dcls_end_day',
            field=models.IntegerField(null=True),
        ),
    ]
