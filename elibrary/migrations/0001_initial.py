# Generated by Django 5.0.4 on 2024-04-11 12:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=500)),
                ('preview', models.TextField()),
                ('content', models.TextField()),
                ('publisher', models.CharField(max_length=500)),
                ('date_published', models.DateField()),
                ('isbn', models.CharField(max_length=500)),
                ('review', models.TextField(blank=True, null=True)),
                ('no_available_books', models.PositiveIntegerField()),
                ('borrowed_books', models.IntegerField()),
                ('file_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elibrary.filetype')),
                ('genere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elibrary.genere')),
            ],
        ),
    ]
