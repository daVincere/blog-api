# Generated by Django 2.2.7 on 2019-11-08 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191108_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(related_name='is_following', to='accounts.Profile'),
        ),
    ]
