# Generated by Django 4.0.6 on 2022-08-06 06:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('legs', '0002_alter_leg_airline_id'),
        ('itineraries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItineraryLegs',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='itinerary',
            name='legs',
            field=models.ManyToManyField(related_name='itineraries', through='itineraries.ItineraryLegs', to='legs.leg'),
        ),
        migrations.AddField(
            model_name='itinerarylegs',
            name='itineraries',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itinerary_legs', to='itineraries.itinerary'),
        ),
        migrations.AddField(
            model_name='itinerarylegs',
            name='legs',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itinerary_legs', to='legs.leg'),
        ),
    ]
