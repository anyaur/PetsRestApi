# Generated by Django 3.2.3 on 2021-05-25 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_alter_pet_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='photos',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
