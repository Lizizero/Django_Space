# Generated by Django 4.1 on 2022-10-21 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="zyxx",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("zsdm", models.CharField(max_length=8)),
                ("zymc", models.CharField(max_length=8)),
                ("level", models.CharField(max_length=8)),
                ("charge", models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name="lqxx",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("zkzh", models.CharField(max_length=8)),
                ("name", models.CharField(max_length=8)),
                (
                    "lqzy",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="luqu.zyxx",
                    ),
                ),
            ],
        ),
    ]
