# Generated by Django 5.1.2 on 2024-10-14 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_tag_project_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('icon', models.CharField(choices=[('github', 'GitHub'), ('web', 'Web')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=20)),
                ('value', models.CharField(max_length=20)),
                ('label', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='links',
            field=models.ManyToManyField(to='api.projectlink'),
        ),
        migrations.AddField(
            model_name='project',
            name='stats',
            field=models.ManyToManyField(to='api.projectstat'),
        ),
    ]
