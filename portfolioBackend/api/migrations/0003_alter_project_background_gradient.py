# Generated by Django 5.1.2 on 2024-10-14 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_project_background_gradient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='background_gradient',
            field=models.CharField(default='background: linear-gradient(to right, #0f0c29, #302b63, #24243e);', max_length=100),
        ),
    ]
