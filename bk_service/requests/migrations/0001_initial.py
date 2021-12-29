# Generated by Django 3.2 on 2021-12-29 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('banks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShareRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('amount', models.DecimalField(decimal_places=4, default=0.0, max_digits=10)),
                ('approval_status', models.CharField(choices=[('pending', 'Pending'), ('rejected', 'Rejected'), ('approved', 'Approved')], max_length=8)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='banks.bank')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='banks.partner')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentScheduleRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('amount', models.DecimalField(decimal_places=4, default=0.0, max_digits=10)),
                ('approval_status', models.CharField(choices=[('pending', 'Pending'), ('rejected', 'Rejected'), ('approved', 'Approved')], max_length=8)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='banks.bank')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='banks.partner')),
                ('schedule_installment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='banks.scheduleinstallment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CreditRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('amount', models.DecimalField(decimal_places=4, default=0.0, max_digits=10)),
                ('approval_status', models.CharField(choices=[('pending', 'Pending'), ('rejected', 'Rejected'), ('approved', 'Approved')], max_length=8)),
                ('installments', models.PositiveIntegerField(default=0)),
                ('credit_use', models.CharField(choices=[('GenerationIncome', 'Generationincome'), ('FamilyStrengthening', 'Familystrengthening'), ('Consumption', 'Consumption')], max_length=40)),
                ('credit_use_detail', models.CharField(choices=[('Trade', 'Trade'), ('Smallcompany', 'Smallcompany'), ('HousingImprovement', 'Housingimprovement'), ('Education', 'Education'), ('HouseholdEquipment', 'Householdequipment'), ('Health', 'Health'), ('Debtpayment', 'Debtpayment'), ('ServicesPay', 'Servicespay'), ('FoodAndClothing', 'Foodandclothing'), ('Transport', 'Transport'), ('Travels', 'Travels'), ('Recreation', 'Recreation')], max_length=40)),
                ('payment_type', models.CharField(choices=[('advanceInstallments', 'Advanceinstallments'), ('installments', 'Installments')], max_length=40)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='banks.bank')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='banks.partner')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
