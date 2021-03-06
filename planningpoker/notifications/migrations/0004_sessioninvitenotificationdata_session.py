# Generated by Django 3.2.4 on 2021-06-21 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planningsessions', '0002_alter_vote_point'),
        ('notifications', '0003_projectinvitenotificationdata_sessioninvitenotificationdata_storycommentnotificationdata_storynotifi'),
    ]

    operations = [
        migrations.AddField(
            model_name='sessioninvitenotificationdata',
            name='session',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='planningsessions.planningsession', to_field='id'),
            preserve_default=False,
        ),
    ]
