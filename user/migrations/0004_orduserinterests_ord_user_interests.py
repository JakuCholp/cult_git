# Generated by Django 4.2.6 on 2023-10-09 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_min_age'),
        ('user', '0003_ord_user_is_busy_organizer_is_busy_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdUserInterests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event_category')),
                ('ord_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.ord_user')),
            ],
        ),
        migrations.AddField(
            model_name='ord_user',
            name='interests',
            field=models.ManyToManyField(through='user.OrdUserInterests', to='events.event_category'),
        ),
    ]