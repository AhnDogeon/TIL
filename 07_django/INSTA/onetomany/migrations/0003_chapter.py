# Generated by Django 2.1.7 on 2019-04-15 16:12

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('onetomany', '0002_auto_20190415_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onetomany.Book')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
