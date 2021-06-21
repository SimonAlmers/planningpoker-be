# Generated by Django 3.2.4 on 2021-06-20 16:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectInviteCode',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='invite_code', to='projects.project', to_field='id')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
