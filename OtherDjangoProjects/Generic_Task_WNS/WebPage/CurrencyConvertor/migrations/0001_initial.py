# Generated by Django 4.2.3 on 2023-08-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Currency_name', models.CharField(max_length=10)),
                ('RoE', models.FloatField()),
            ],
        ),
    ]