# Generated by Django 4.2 on 2023-05-04 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traduction',
            name='francais',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
