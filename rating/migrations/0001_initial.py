# Generated by Django 4.0.1 on 2022-03-07 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('tmdb_id', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
