# Generated by Django 4.1.7 on 2023-04-27 09:26

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0004_subcategories_subcat_alter_subcategories_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Size",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                (
                    "unique_id",
                    models.CharField(
                        blank=True, max_length=200, null=True, unique=True
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("price", models.FloatField()),
                ("total_stock", models.PositiveIntegerField()),
                ("image", models.ImageField(upload_to="product-img/")),
                ("description", ckeditor.fields.RichTextField(null=True)),
                (
                    "created_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "condition",
                    models.CharField(
                        choices=[("New", "New"), ("Old", "Old")], max_length=100
                    ),
                ),
                (
                    "stock",
                    models.CharField(
                        choices=[
                            ("IN STOCK", "IN STOCK"),
                            ("OUT OF STOCK", "OUT OF STOCK"),
                        ],
                        max_length=200,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("PUBLISH", "PUBLISH"), ("DRAFT", "DRAFT")],
                        max_length=200,
                    ),
                ),
                (
                    "categories",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1.categories",
                    ),
                ),
                ("sizes", models.ManyToManyField(to="app1.size")),
                (
                    "subcategories",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app1.subcategories",
                    ),
                ),
            ],
        ),
    ]
