# Generated by Django 2.0 on 2021-01-13 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0005_auto_20210113_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='TypeAnswer',
            field=models.CharField(choices=[('OPEN', 'Open'), ('CLOSED', 'Closed')], max_length=1, null=True),
        ),
    ]
