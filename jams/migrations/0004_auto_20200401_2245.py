# Generated by Django 3.0.4 on 2020-04-01 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0003_auto_20200401_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jam',
            name='open_tok_session_id',
            field=models.CharField(default=None, max_length=250),
        ),
    ]