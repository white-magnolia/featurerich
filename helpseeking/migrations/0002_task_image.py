# Generated by Django 2.0.6 on 2018-07-05 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpseeking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='task_images/'),
        ),
    ]