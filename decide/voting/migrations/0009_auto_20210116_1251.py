# Generated by Django 2.0 on 2021-01-16 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0008_auto_20210114_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voting',
            name='themeVotation',
            field=models.CharField(blank=True, choices=[('El', 'Electoral'), ('Si', 'Self-interest'), ('Kw', 'Knowledge'), ('Ts', 'Testing'), ('Su', 'Survey')], max_length=14, null=True),
        ),
    ]
