# Generated by Django 4.2.6 on 2023-10-06 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('rating', models.IntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('ord_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.ord_user')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.organizer')),
            ],
        ),
    ]