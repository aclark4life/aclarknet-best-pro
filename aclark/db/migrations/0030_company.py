# Generated by Django 2.2.3 on 2019-07-30 18:19

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ("taggit", "0003_taggeditem_add_unique_index"),
        ("db", "0029_auto_20190709_1202"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("active", models.BooleanField(default=True)),
                ("hidden", models.BooleanField(default=False)),
                ("published", models.BooleanField(default=False)),
                ("name", models.CharField(blank=True, max_length=300, null=True)),
                ("address", models.TextField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("url", models.URLField(blank=True, null=True, verbose_name="Website")),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        blank=True,
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
            ],
            options={"ordering": ["name"]},
        )
    ]