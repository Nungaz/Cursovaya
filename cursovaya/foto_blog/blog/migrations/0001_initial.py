# Generated by Django 5.0.1 on 2024-04-07 17:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'категорию',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('slug', models.SlugField(max_length=260, unique=True, verbose_name='URL')),
                ('body', models.TextField(blank=True, verbose_name='Контент')),
                ('photo', models.ImageField(blank=True, upload_to='photo/%Y/%m/%d/', verbose_name='Фото')),
                ('time_cre', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('time_up', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('published', models.BooleanField(default=True, verbose_name='Публикация')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-time_cre'],
            },
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_image', models.ImageField(blank=True, null=True, upload_to='photo/%Y/%m/%d/add/', verbose_name='Добавить картинку')),
                ('image', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blog', verbose_name='картинки')),
            ],
            options={
                'verbose_name': 'изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]