# Generated by Django 3.0.8 on 2020-07-09 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='help_text',
            field=models.CharField(max_length=256, null=True, verbose_name='Текст помощи'),
        ),
    ]
