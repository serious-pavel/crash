# Generated by Django 4.0.6 on 2022-07-21 18:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crash_core', '0007_alter_frame_update_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frame',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 21, 18, 17, 34, 912197, tzinfo=utc)),
        ),
    ]
