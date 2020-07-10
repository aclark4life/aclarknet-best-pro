# Generated by Django 3.0.7 on 2020-07-10 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0048_auto_20200710_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='interest',
            field=models.DecimalField(blank=True, decimal_places=2, default=2.5, max_digits=12, null=True, verbose_name='Interest'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='principal',
            field=models.DecimalField(blank=True, decimal_places=2, default=400000.0, max_digits=12, null=True, verbose_name='Principal'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='term',
            field=models.IntegerField(blank=True, null=True, verbose_name='Term'),
        ),
    ]
