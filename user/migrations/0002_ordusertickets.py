# Generated by Django 4.2.6 on 2023-10-10 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdUserTickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tickets', models.ImageField(default='tickets/QR-cod1.png', upload_to='')),
                ('ord_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.ord_user')),
            ],
        ),
    ]
