# Generated by Django 4.0.4 on 2022-07-20 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_alter_menti_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menti',
            name='status',
            field=models.CharField(choices=[('start', 'start'), ('end', 'end')], default='end', max_length=100),
        ),
    ]
