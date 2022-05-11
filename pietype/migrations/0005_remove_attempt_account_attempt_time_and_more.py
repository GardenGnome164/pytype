# Generated by Django 4.0.4 on 2022-05-11 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pietype', '0004_attempt_sentence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attempt',
            name='account',
        ),
        migrations.AddField(
            model_name='attempt',
            name='time',
            field=models.CharField(default='00:00', max_length=20, verbose_name='Time Elapsed'),
        ),
        migrations.AlterField(
            model_name='attempt',
            name='raw_wpm',
            field=models.IntegerField(verbose_name='Raw WPM'),
        ),
    ]
