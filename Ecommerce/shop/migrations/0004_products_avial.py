# Generated by Django 2.2 on 2021-12-30 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20211230_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='avial',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
