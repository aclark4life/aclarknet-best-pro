# Generated by Django 2.2 on 2019-05-01 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("db", "0009_workorder")]

    operations = [migrations.RenameModel(old_name="WorkOrder", new_name="Order")]