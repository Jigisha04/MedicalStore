# Generated by Django 3.2.15 on 2025-04-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='health',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=30)),
                ('hprice', models.IntegerField()),
                ('hinfo', models.TextField()),
                ('hamm', models.CharField(max_length=30, null=True)),
                ('himg', models.ImageField(upload_to='static/imagesv/')),
            ],
        ),
        migrations.CreateModel(
            name='medicines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=30)),
                ('mprice', models.IntegerField()),
                ('minfo', models.TextField()),
                ('mamm', models.CharField(max_length=30, null=True)),
                ('mimg', models.ImageField(upload_to='static/imagesg/')),
            ],
        ),
    ]
