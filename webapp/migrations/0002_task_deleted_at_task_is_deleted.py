# Generated by Django 4.1.1 on 2022-09-30 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True, verbose_name='Date deleted'),
        ),
        migrations.AddField(
            model_name='task',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Deleted'),
        ),
    ]
