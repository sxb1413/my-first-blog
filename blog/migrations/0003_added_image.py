# Generated by Django 2.2.12 on 2020-06-04 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_added_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.png', upload_to='imageUploads'),
        ),
    ]
