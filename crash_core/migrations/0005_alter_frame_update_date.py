# Generated by Django 4.0.6 on 2022-07-21 17:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crash_core', '0004_alter_frame_update_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frame',
            name='update_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
