# Generated by Django 4.2.6 on 2023-10-05 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_middle_name_ord_user_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ord_user',
            name='email_token',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
