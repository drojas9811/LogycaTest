# Generated by Django 4.0 on 2022-07-08 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventarioapp', '0004_alter_inventario_clientefk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='fecha',
            field=models.DateField(verbose_name='FechaPa'),
        ),
    ]
