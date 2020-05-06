# Generated by Django 3.0.5 on 2020-05-06 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Time when instance was created.', verbose_name='create time')),
                ('deleted_at', models.DateTimeField(blank=True, help_text='Time when instance was deleted.', null=True, verbose_name='delete time')),
                ('last_update_at', models.DateTimeField(auto_now=True, help_text='Time when isinstance was updted.', null=True, verbose_name='last update')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Time when instance was created.', verbose_name='create time')),
                ('deleted_at', models.DateTimeField(blank=True, help_text='Time when instance was deleted.', null=True, verbose_name='delete time')),
                ('last_update_at', models.DateTimeField(auto_now=True, help_text='Time when isinstance was updted.', null=True, verbose_name='last update')),
                ('name_eng', models.CharField(max_length=100)),
                ('name_rus', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
