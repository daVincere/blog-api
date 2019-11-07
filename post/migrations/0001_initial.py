# Generated by Django 2.2.7 on 2019-11-07 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import post.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=150)),
                ('photo', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=post.models.upload_location, width_field='width_field')),
                ('width_field', models.IntegerField(default=0, null=True)),
                ('height_field', models.IntegerField(default=0, null=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
