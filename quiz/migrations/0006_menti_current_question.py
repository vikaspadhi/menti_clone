# Generated by Django 4.0.4 on 2022-07-22 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_alter_player_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='menti',
            name='current_question',
            field=models.IntegerField(default=0),
        ),
    ]
