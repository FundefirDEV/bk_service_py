# Generated by Django 3.2 on 2022-01-28 19:18

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
                ('name', models.CharField(error_messages={'invalid': 'error_message : The bank name is invalid., error_code : 36', 'required': 'error_message : The bank name is required., error_code : 27', 'unique': 'error_message : This bank name already exists., error_code : 28'}, max_length=30, unique=True)),
                ('cash_balance', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('active_credits', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('shares', models.PositiveIntegerField(default=0)),
                ('expenditure_fund', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('reserve_fund_of_bad_debt', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
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
                ('ordinary_interest', models.DecimalField(decimal_places=4, default=3.0, max_digits=10)),
                ('delay_interest', models.DecimalField(decimal_places=4, default=5.0, max_digits=10)),
                ('maximun_credit_installments', models.PositiveIntegerField(default=3)),
                ('maximun_credit_value', models.DecimalField(decimal_places=4, default=1000000.0, max_digits=100)),
                ('share_value', models.DecimalField(decimal_places=4, default=10000, max_digits=100)),
                ('maximum_shares_percentage_per_partner', models.DecimalField(decimal_places=4, default=25.0, max_digits=100)),
                ('maximum_active_credits_per_partner', models.DecimalField(decimal_places=4, default=1, max_digits=100)),
                ('expenditure_fund_percentage', models.DecimalField(decimal_places=4, default=5.0, max_digits=10)),
                ('reserve_fund_of_bad_debt_percentage', models.DecimalField(decimal_places=4, default=5.0, max_digits=10)),
                ('payment_period_of_installment', models.PositiveIntegerField(default=30)),
                ('credit_investment_relationship', models.DecimalField(decimal_places=4, default=5, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
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
                ('credit_use', models.CharField(choices=[('generationIncome', 'Generationincome'), ('familyStrengthening', 'Familystrengthening'), ('consumption', 'Consumption')], max_length=40)),
                ('credit_use_detail', models.CharField(choices=[('trade', 'Trade'), ('Smallcompany', 'Smallcompany'), ('HousingImprovement', 'Housingimprovement'), ('Education', 'Education'), ('HouseholdEquipment', 'Householdequipment'), ('Health', 'Health'), ('Debtpayment', 'Debtpayment'), ('ServicesPay', 'Servicespay'), ('FoodAndClothing', 'Foodandclothing'), ('Transport', 'Transport'), ('Travels', 'Travels'), ('Recreation', 'Recreation')], max_length=40)),
                ('payment_type', models.CharField(choices=[('advance', 'Advance'), ('installments', 'Installments')], max_length=40)),
                ('total_interest', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
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
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('total_shares_quantity', models.PositiveIntegerField(default=0)),
                ('total_credits_quantity', models.PositiveIntegerField(default=0)),
                ('total_shares_amount', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('total_credits_amount', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('total_ordinary_interest', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('total_capital', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('total_delay_interest', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('earning_by_share', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('expenditure_fund', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('reserve_fund_of_bad_debt', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('phone_number', models.CharField(error_messages={'invalid': 'error_message : The phone number is invalid., error_code : 12', 'required': 'error_message : The phone number is required., error_code : 7', 'unique': 'error_message : This phone number already exists., error_code : 2'}, max_length=18, unique=True, validators=[django.core.validators.MinLengthValidator(4)])),
                ('phone_region_code', models.CharField(error_messages={'required': 'error_message : The phone region code is required., error_code : 10'}, max_length=4, validators=[django.core.validators.RegexValidator(message='error_message : The phone region code is invalid., error_code : 13', regex='\\+?1?\\d{0,9}$'), django.core.validators.MinLengthValidator(1)])),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('partner', 'Partner'), ('guest', 'Guest')], error_messages={'invalid': 'error_message : The partner role is invalid., error_code : 41', 'required': 'error_message : The partner role is required., error_code : 42'}, max_length=8)),
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
                ('document_number', models.CharField(blank=True, max_length=30)),
                ('profession', models.CharField(blank=True, max_length=150)),
                ('scholarship', models.CharField(choices=[('noData', 'Nodata'), ('primary', 'Primary'), ('secondary', 'Secondary'), ('highschool', 'Highschool'), ('university', 'University'), ('master', 'Master'), ('doctorate', 'Doctorate')], default='noData', max_length=30)),
                ('birth_date', models.DateTimeField(null=True)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'get_latest_by': 'created_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PartnerGuest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created', verbose_name='create at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified', verbose_name='modified at')),
                ('phone_number', models.CharField(error_messages={'invalid': 'error_message : The partner guest name is invalid., error_code : 33', 'required': 'error_message : The partner guest name is required., error_code : 29', 'unique': 'error_message : This partner guest phone already exists., error_code : 31'}, max_length=18, unique=True, validators=[django.core.validators.MinLengthValidator(4)])),
                ('name', models.CharField(error_messages={'invalid': 'error_message : The partner guest name is invalid., error_code : 33', 'required': 'error_message : The partner guest name is required., error_code : 29'}, max_length=150, validators=[django.core.validators.MinLengthValidator(2)])),
                ('phone_region_code', models.CharField(error_messages={'required': 'error_message : The partner guest phone region code is required., error_code : 32'}, max_length=4, validators=[django.core.validators.RegexValidator(message='error_message : The partner guest phone region code is invalid., error_code : 35', regex='\\+?1?\\d{0,9}$'), django.core.validators.MinLengthValidator(1)])),
                ('is_active', models.BooleanField(default=False)),
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
                ('interest_paid', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('capital_paid', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
            ],
            options={
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
                ('amount_paid', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('payment_date', models.DateTimeField()),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('complete', 'Complete'), ('incomplete', 'Incomplete')], default='pending', max_length=20)),
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
                ('quantity', models.PositiveIntegerField(default=0)),
                ('amount', models.DecimalField(decimal_places=4, default=0.0, max_digits=100)),
                ('is_active', models.BooleanField(default=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='banks.bank')),
                ('meeting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='banks.meeting')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='banks.partner')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
