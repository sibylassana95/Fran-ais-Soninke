# Generated by Django 4.2 on 2023-04-18 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Traduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('francais', models.CharField(max_length=255)),
                ('soninke', models.CharField(max_length=255)),
            ],
        ),
    ]
