# Generated by Django 2.2.5 on 2019-10-01 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoblog', '0008_auto_20191001_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
