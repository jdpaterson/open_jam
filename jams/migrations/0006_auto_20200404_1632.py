# Generated by Django 3.0.4 on 2020-04-04 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0005_auto_20200403_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jam',
            name='open_tok_session_id',
            field=models.CharField(default='2_MX40NjU5MzM4Mn5-MTU4NjAxNzk3MjAxOH5EdllINXQ3SytTL1JobFkrZnUwVUd4MVN-fg', max_length=250),
        ),
    ]
