# Generated by Django 3.2.9 on 2021-11-30 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='interesses',
        ),
        migrations.AddField(
            model_name='aluno',
            name='interesses',
            field=models.ManyToManyField(null=True, to='pages.Interesses'),
        ),
    ]
