# Generated by Django 3.2 on 2022-02-02 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('requests', '0001_initial'),
        ('banks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='share_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='requests.sharerequest'),
        ),
        migrations.AddField(
            model_name='scheduleinstallment',
            name='credit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='banks.credit'),
        ),
        migrations.AddField(
            model_name='paymentschedule',
            name='bank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='banks.bank'),
        ),
        migrations.AddField(
            model_name='paymentschedule',
            name='meeting',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='banks.meeting'),
        ),
        migrations.AddField(
            model_name='paymentschedule',
            name='partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='banks.partner'),
        ),
        migrations.AddField(
            model_name='paymentschedule',
            name='payment_schedule_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='requests.paymentschedulerequest'),
        ),
        migrations.AddField(
            model_name='partnerguest',
            name='bank',
            field=models.ForeignKey(error_messages={'does_not_exist': 'error_message : The bank is invalid., error_code : 37', 'required': 'error_message : The bank is required., error_code : 38'}, on_delete=django.db.models.deletion.PROTECT, to='banks.bank'),
        ),
        migrations.AddField(
            model_name='partnerdetail',
            name='partner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='banks.partner'),
        ),
        migrations.AddField(
            model_name='partner',
            name='bank',
            field=models.ForeignKey(error_messages={'does_not_exist': 'error_message : The bank is invalid., error_code : 37', 'required': 'error_message : The bank is required., error_code : 38'}, on_delete=django.db.models.deletion.PROTECT, to='banks.bank'),
        ),
    ]
