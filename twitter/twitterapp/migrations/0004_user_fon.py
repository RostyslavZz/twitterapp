# Generated by Django 4.2.5 on 2023-11-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterapp', '0003_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fon',
            field=models.ImageField(default='media/avatar/basefon.png', upload_to='media/avatar/'),
        ),
    ]
