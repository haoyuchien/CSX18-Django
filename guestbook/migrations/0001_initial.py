# Generated by Django 2.1.1 on 2018-10-05 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TourDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('venue', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
    ]
