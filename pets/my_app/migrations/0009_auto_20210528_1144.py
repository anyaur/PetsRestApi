# Generated by Django 3.2.3 on 2021-05-28 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_pet_photos'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(max_length=255, upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='pet',
            name='photos',
            field=models.ImageField(default='default.jpg', upload_to='images/'),
        ),
    ]
