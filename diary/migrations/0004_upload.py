# Generated by Django 3.0.5 on 2021-05-23 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_auto_20210521_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
