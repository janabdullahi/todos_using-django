# Generated by Django 2.2.12 on 2022-08-17 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20220817_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Completed Date'),
        ),
    ]
