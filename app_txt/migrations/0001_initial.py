# Generated by Django 4.2.4 on 2023-09-08 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.TextField(max_length=255)),
                ('password', models.IntegerField()),
            ],
        ),
    ]
