# Generated by Django 5.1.2 on 2024-10-14 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_projectlink_name_projectlink_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectstat',
            name='label',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
