# Generated by Django 3.2.15 on 2022-10-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='scores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kh', models.CharField(max_length=8)),
                ('xm', models.CharField(max_length=8)),
                ('yw', models.SmallIntegerField()),
                ('sx', models.SmallIntegerField()),
                ('bj', models.CharField(max_length=8)),
            ],
        ),
    ]