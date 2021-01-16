# Generated by Django 2.0 on 2021-01-16 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0010_auto_20210116_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='scopes',
            field=models.CharField(blank=True, choices=[('Lit', 'Literature'), ('Ent', 'Entertainment'), ('Geo', 'Geography'), ('His', 'History'), ('Sci', 'Science'), ('Spo', 'Sports'), ('Oth', 'Other')], max_length=4, null=True),
        ),
    ]
