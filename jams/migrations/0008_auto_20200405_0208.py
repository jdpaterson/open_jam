# Generated by Django 3.0.4 on 2020-04-05 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0007_auto_20200404_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jam',
            name='open_tok_session_id',
        ),
        migrations.AddField(
            model_name='jam',
            name='opentok_session_id',
            field=models.CharField(default='2_MX40NjU5MzM4Mn5-MTU4NjA1MjUzMjk4Nn5qTEFFeDZ4Vmk3TldGMGxCWHBDTjQ0dVp-fg', max_length=250),
        ),
    ]
