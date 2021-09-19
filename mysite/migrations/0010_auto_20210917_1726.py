# Generated by Django 3.2.7 on 2021-09-17 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0009_alter_profile_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_updated_time',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='repositories',
        ),
        migrations.AddField(
            model_name='profile',
            name='last_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.DeleteModel(
            name='repository',
        ),
    ]
