# Generated by Django 4.0.2 on 2022-03-17 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_links', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='name',
            field=models.CharField(choices=[('facebook', 'Facebook'), ('instagram', 'Instagram'), ('youtube', 'YouTube'), ('twitter', 'Twitter'), ('spotify', 'Spotify'), ('reddit', 'Reddit')], max_length=300),
        ),
    ]
