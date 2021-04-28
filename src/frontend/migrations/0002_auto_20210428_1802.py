# Generated by Django 3.2 on 2021-04-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enter_url',
            name='url',
        ),
        migrations.AddField(
            model_name='enter_url',
            name='geeks_field',
            field=models.URLField(default=True),
            preserve_default=False,
        ),
    ]