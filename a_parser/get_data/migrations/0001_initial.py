# Generated by Django 3.2 on 2021-04-15 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('data', models.CharField(max_length=25)),
                ('method', models.CharField(max_length=4)),
                ('url', models.TextField()),
                ('response', models.IntegerField()),
                ('response_size', models.IntegerField()),
            ],
        ),
    ]