# Generated by Django 3.1.6 on 2023-01-17 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpost_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ManyToManyField(to='blog.Category'),
        ),
    ]
