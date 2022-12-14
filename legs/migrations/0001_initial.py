# Generated by Django 4.0.6 on 2022-08-05 04:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leg',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('departure_airport', models.CharField(max_length=32)),
                ('arrival_airport', models.CharField(max_length=32)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('stops', models.IntegerField(default=1)),
                ('airline_name', models.CharField(max_length=32)),
                ('airline_id', models.CharField(max_length=32, unique=True)),
                ('duration_mins', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
