# Generated by Django 3.1.3 on 2022-02-05 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220204_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
