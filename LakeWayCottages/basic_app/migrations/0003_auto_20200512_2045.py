# Generated by Django 3.0.4 on 2020-05-12 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_auto_20200512_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('desc', models.TextField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='indexModel',
        ),
    ]
