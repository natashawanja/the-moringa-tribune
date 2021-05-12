# Generated by Django 3.2.2 on 2021-05-12 12:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210512_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default=datetime.datetime(2021, 5, 12, 12, 21, 36, 89405, tzinfo=utc), upload_to='articles/'),
            preserve_default=False,
        ),
    ]