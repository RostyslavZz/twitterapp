# Generated by Django 4.2.5 on 2023-09-11 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitterapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createat', models.DateTimeField(auto_now_add=True)),
                ('modifiedat', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/postimages/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createat', models.DateTimeField(auto_now_add=True)),
                ('modifiedat', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitterapp.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createat', models.DateTimeField(auto_now_add=True)),
                ('modifiedat', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=255)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitterapp.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
