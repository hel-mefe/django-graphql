# Generated by Django 4.2.10 on 2024-02-26 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game', '0001_initial'),
        ('user_settings', '0001_initial'),
        ('friendship', '0001_initial'),
        ('tournament', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('friends', models.ManyToManyField(to='friendship.friendship')),
                ('games', models.ManyToManyField(to='game.game')),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='user_settings.usersettings')),
                ('tournaments', models.ManyToManyField(to='tournament.tournament')),
            ],
        ),
    ]
