# Generated by Django 4.2.6 on 2023-10-10 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='location_for_map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=255)),
                ('lon', models.FloatField()),
                ('lat', models.FloatField()),
            ],
        ),
    ]