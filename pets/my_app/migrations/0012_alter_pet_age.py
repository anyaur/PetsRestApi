# Generated by Django 3.2.3 on 2021-05-28 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0011_delete_myimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='age',
            field=models.IntegerField(),
        ),
    ]