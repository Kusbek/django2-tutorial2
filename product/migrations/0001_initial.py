# Generated by Django 2.2.6 on 2019-10-15 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('votes_total', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('icon', models.ImageField(upload_to='images/')),
                ('body', models.TextField()),
            ],
        ),
    ]
