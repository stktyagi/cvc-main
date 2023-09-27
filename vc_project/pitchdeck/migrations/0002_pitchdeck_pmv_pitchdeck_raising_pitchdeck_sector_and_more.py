# Generated by Django 4.2.2 on 2023-09-24 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pitchdeck', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pitchdeck',
            name='PMV',
            field=models.BigIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='pitchdeck',
            name='Raising',
            field=models.BigIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='pitchdeck',
            name='Sector',
            field=models.CharField(default='NONE', max_length=100),
        ),
        migrations.AddField(
            model_name='pitchdeck',
            name='assur',
            field=models.CharField(choices=[('SEIS', 'SEIS'), ('EIS', 'EIS'), ('NONE', 'NONE')], default='NONE', max_length=6),
        ),
        migrations.AddField(
            model_name='pitchdeck',
            name='email',
            field=models.EmailField(default='NONE', max_length=254),
        ),
        migrations.AddField(
            model_name='pitchdeck',
            name='location',
            field=models.CharField(default='NONE', max_length=100),
        ),
    ]
