# Generated by Django 4.2.6 on 2023-10-09 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_creator'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='min_age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
