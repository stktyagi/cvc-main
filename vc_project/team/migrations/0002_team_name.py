# Generated by Django 4.2.2 on 2023-07-17 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]