# Generated by Django 4.1.5 on 2023-01-30 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_event_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='orgniser_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]