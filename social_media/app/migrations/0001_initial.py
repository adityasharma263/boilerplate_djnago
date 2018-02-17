# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('post_text', models.TextField(max_length=80)),
                ('published_on', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'post',
                'ordering': ('-updated_at',),
                'default_permissions': ('add', 'change', 'delete', 'view'),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('mobile', models.BigIntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(7000000000)], null=True)),
                ('email', models.EmailField(blank=True, max_length=300, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('follows', models.ManyToManyField(to='app.User')),
            ],
            options={
                'db_table': 'user',
                'ordering': ('-updated_at',),
                'default_permissions': ('add', 'change', 'delete', 'view'),
            },
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(to='app.User', related_name='user_post'),
        ),
    ]
