# Generated by Django 4.2.11 on 2024-05-10 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_ratingmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratingmodel',
            old_name='movieTitle',
            new_name='movie',
        ),
    ]
