# Generated by Django 2.1.1 on 2018-09-25 13:39

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [("db", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="dashboard_items",
            field=multiselectfield.db.fields.MultiSelectField(
                blank=True,
                choices=[("times", "Times"), ("totals", "Totals")],
                max_length=12,
                null=True,
                verbose_name="Dashboard Items",
            ),
        )
    ]
