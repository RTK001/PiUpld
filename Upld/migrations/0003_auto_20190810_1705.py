# Generated by Django 2.1.7 on 2019-08-10 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Upld', '0002_auto_20190804_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='githubproject',
            name='git_link',
            field=models.URLField(),
        ),
    ]
