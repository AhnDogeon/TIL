# Generated by Django 2.1.7 on 2019-04-19 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mton', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='hotel',
            name='clients',
            field=models.ManyToManyField(related_name='hotels', to='mton.Client'),
        ),
    ]
