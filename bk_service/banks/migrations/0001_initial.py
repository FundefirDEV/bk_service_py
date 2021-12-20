# Generated by Django 3.2 on 2021-12-20 20:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('cash_balance', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('active_credits', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('shares', models.PositiveIntegerField(default=0)),
                ('expense_fund', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('bad_debt_reserve', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BankRules',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('ordinary_interest', models.DecimalField(decimal_places=4, default=0.0, max_digits=10)),
                ('delay_interest', models.DecimalField(decimal_places=4, default=0.0, max_digits=10)),
                ('maximun_credit_installments', models.PositiveIntegerField(default=0)),
                ('maximun_credit_value', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('share_value', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('is_active', models.BooleanField(default=True)),
                ('expenditure_fund_percentage', models.DecimalField(decimal_places=4, default=0.0, max_digits=10)),
                ('reserve_fund_of_bad_debt', models.DecimalField(decimal_places=4, default=0.0, max_digits=10)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('installments', models.PositiveIntegerField(default=1)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=100)),
                ('credit_use', models.CharField(choices=[('GenerationIncome', 'Generationincome'), ('FamilyStrengthening', 'Familystrengthening'), ('Consumption', 'Consumption')], max_length=40)),
                ('creadit_use_detail', models.CharField(choices=[('Trade', 'Trade'), ('Smallcompany', 'Smallcompany'), ('HousingImprovement', 'Housingimprovement'), ('Education', 'Education'), ('HouseholdEquipment', 'Householdequipment'), ('Health', 'Health'), ('Debtpayment', 'Debtpayment'), ('ServicesPay', 'Servicespay'), ('FoodAndClothing', 'Foodandclothing'), ('Transport', 'Transport'), ('Travels', 'Travels'), ('Recreation', 'Recreation')], max_length=40)),
                ('payment_type', models.CharField(choices=[('advanceInstallments', 'Advanceinstallments'), ('installments', 'Installments')], max_length=40)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EarningShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('earning_by_share', models.DecimalField(decimal_places=4, max_digits=100)),
                ('total_earning_by_share', models.DecimalField(decimal_places=4, max_digits=100)),
                ('is_paid', models.BooleanField(default=False)),
                ('date_calculated', models.DateTimeField()),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_meeting', models.DateTimeField(auto_now_add=True)),
                ('total_shares', models.PositiveIntegerField(default=0)),
                ('total_credit', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('total_ordinary_interest', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('total_capital', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('total_delay_interest', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('earning_by_shares', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('balance', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('expenditure_fund', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('reserve_fund_bad_debts', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('phone_number', models.CharField(max_length=18, unique=True, validators=[django.core.validators.MinLengthValidator(4)])),
                ('phone_region_code', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(message='region code must be entered in the format +999.', regex='\\+?1?\\d{0,9}$'), django.core.validators.MinLengthValidator(4)])),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('partner', 'Partner'), ('guest', 'Guest')], max_length=8)),
                ('temporal_name', models.CharField(blank=True, max_length=150)),
                ('is_active', models.BooleanField(default=True)),
                ('is_creator', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PartnerDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('earnings', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('active_credit', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('shares', models.PositiveIntegerField(default=0)),
                ('document_number', models.CharField(blank=True, max_length=30, unique=True)),
                ('profession', models.CharField(blank=True, max_length=150)),
                ('scholarship', models.CharField(choices=[('noData', 'Nodata'), ('primary', 'Primary'), ('secundary', 'Secundary'), ('highschool', 'Highschool'), ('university', 'University'), ('master', 'Master'), ('doctorate', 'Doctorate')], default='noData', max_length=30)),
                ('birth_date', models.DateTimeField()),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('amount', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('date', models.DateTimeField()),
                ('interest_paid', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('capital_paid', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ScheduleInstallment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('capital_installment', models.DecimalField(decimal_places=4, max_digits=100)),
                ('ordinary_interest_percentage', models.DecimalField(decimal_places=4, max_digits=100)),
                ('interest_calculated', models.DecimalField(decimal_places=4, max_digits=10)),
                ('total_pay_installment', models.DecimalField(decimal_places=4, max_digits=100)),
                ('payment_date', models.DateTimeField()),
                ('payment_status', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('quantity', models.PositiveIntegerField(default=0.0)),
                ('amount', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='banks.bank')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='banks.partner')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
    ]
