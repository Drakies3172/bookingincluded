# Generated by Django 3.0.6 on 2020-05-27 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('people', models.TextField(max_length=100)),
                ('room', models.TextField(max_length=100)),
                ('checkinday', models.TextField(max_length=100)),
                ('checkoutday', models.TextField(max_length=100)),
                ('name', models.TextField(max_length=100)),
                ('id_number', models.TextField(max_length=100)),
                ('email', models.TextField(max_length=100)),
                ('phone', models.TextField(max_length=100)),
                ('current_address', models.TextField(max_length=100)),
            ],
        ),
    ]
