# Generated by Django 3.2.3 on 2021-05-25 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_remove_pet_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='photos',
            field=models.ImageField(default='barsik.jpg', upload_to='images/'),
        ),
    ]
