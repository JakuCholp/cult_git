# Generated by Django 4.2.6 on 2023-10-09 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_creator'),
        ('user', '0002_ord_user_country_organizer_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='ord_user',
            name='is_busy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organizer',
            name='is_busy',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='OrganizerUserEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('organizer_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.organizer')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizerInterests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event_category')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.organizer')),
            ],
        ),
        migrations.CreateModel(
            name='OrdUserEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('ord_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.ord_user')),
            ],
        ),
        migrations.AddField(
            model_name='ord_user',
            name='events',
            field=models.ManyToManyField(through='user.OrdUserEvent', to='events.event'),
        ),
        migrations.AddField(
            model_name='organizer',
            name='events',
            field=models.ManyToManyField(through='user.OrganizerUserEvent', to='events.event'),
        ),
        migrations.AddField(
            model_name='organizer',
            name='interests',
            field=models.ManyToManyField(through='user.OrganizerInterests', to='events.event_category'),
        ),
    ]
