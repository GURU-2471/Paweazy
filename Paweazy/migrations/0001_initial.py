# Generated by Django 4.0.4 on 2022-06-12 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pname', models.CharField(max_length=50)),
                ('Oname', models.CharField(max_length=50)),
                ('Email', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=8)),
                ('Moblie', models.CharField(max_length=10)),
                ('Address', models.TextField()),
            ],
        ),
    ]
