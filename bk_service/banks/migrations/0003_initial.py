# Generated by Django 3.2 on 2022-02-15 18:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('banks', '0002_initial'),
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='user',
            field=models.OneToOneField(error_messages={'does_not_exist': 'error_message : The user is invalid., error_code : 39', 'required': 'error_message : The user is required., error_code : 40'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='meeting',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='banks.bank'),
        ),
        migrations.AddField(
            model_name='earningshare',
            name='meeting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.meeting'),
        ),
        migrations.AddField(
            model_name='earningshare',
            name='share',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='banks.share'),
        ),
        migrations.AddField(
            model_name='credit',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='banks.bank'),
        ),
        migrations.AddField(
            model_name='credit',
            name='credit_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requests.creditrequest'),
        ),
        migrations.AddField(
            model_name='credit',
            name='meeting',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='banks.meeting'),
        ),
        migrations.AddField(
            model_name='credit',
            name='partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='banks.partner'),
        ),
        migrations.AddField(
            model_name='bankrules',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='banks.bank'),
        ),
        migrations.AddField(
            model_name='bank',
            name='city',
            field=models.ForeignKey(error_messages={'does_not_exist': 'error_message : The city is invalid., error_code : 16', 'invalid': 'error_message : The city is invalid., error_code : 16', 'required': 'error_message : The city is required., error_code : 15'}, on_delete=django.db.models.deletion.PROTECT, to='locations.city'),
        ),
    ]
