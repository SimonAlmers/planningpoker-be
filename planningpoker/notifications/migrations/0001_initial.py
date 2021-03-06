# Generated by Django 3.2.4 on 2021-06-20 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planningsessions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('kind', models.IntegerField(choices=[(1, 'Project Invite'), (2, 'Session Invite'), (3, 'Session Comment Mention'), (4, 'Story Comment Mention'), (5, 'Story Update')])),
                ('message', models.CharField(max_length=128)),
                ('context', models.CharField(max_length=128)),
                ('read_at', models.DateTimeField(blank=True, null=True)),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, to_field='id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to=settings.AUTH_USER_MODEL, to_field='id')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SessionCommentNotificationData',
            fields=[
                ('notification', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='session_comment', serialize=False, to='notifications.notification', to_field='id')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planningsessions.planningsessioncomment', to_field='id')),
            ],
        ),
    ]
