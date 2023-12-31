# Generated by Django 4.2.6 on 2023-10-09 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('min_age', models.IntegerField()),
                ('location', models.TextField(max_length=255)),
                ('image', models.ImageField(default='events_image/logo.png', upload_to='events_image')),
                ('ticket_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('count_user', models.IntegerField(default=0)),
                ('max_capacity', models.IntegerField()),
                ('duration', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Event_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Event_Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_registered_users', models.IntegerField(blank=True, null=True)),
                ('number_of_arrivals', models.IntegerField()),
                ('was_spent', models.IntegerField()),
                ('was_recived', models.IntegerField(blank=True, null=True)),
                ('income', models.IntegerField(blank=True, null=True)),
                ('more_than_aver', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
    ]
