# Generated by Django 3.2.15 on 2022-10-11 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='faqsdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('sex', models.CharField(blank=True, max_length=2)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
