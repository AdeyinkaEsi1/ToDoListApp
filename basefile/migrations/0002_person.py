# Generated by Django 4.2 on 2023-05-22 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basefile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
            ],
        ),
    ]
