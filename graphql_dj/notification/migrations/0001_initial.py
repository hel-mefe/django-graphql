# Generated by Django 4.2.10 on 2024-02-26 01:19

from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import notification.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('state', enumfields.fields.EnumField(default='PENDING', enum=notification.models.NotificationState, max_length=10)),
                ('userId', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, related_name='notification_user', to='user.user')),
            ],
        ),
    ]
