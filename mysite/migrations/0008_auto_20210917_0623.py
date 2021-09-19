# Generated by Django 3.2.7 on 2021-09-17 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20210917_0510'),
    ]

    operations = [
        migrations.CreateModel(
            name='repository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40)),
                ('stars', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='repositories',
            field=models.ManyToManyField(to='mysite.repository'),
        ),
    ]