# Generated by Django 3.2 on 2021-04-18 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_project_long_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='screenshot',
            field=models.URLField(blank=True),
        ),
    ]
