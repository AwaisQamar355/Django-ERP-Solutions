# Generated by Django 5.0.3 on 2024-07-04 13:08

import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('company_id', models.CharField(max_length=50, unique=True)),
                ('contact_person_name', models.CharField(max_length=255)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_phone_number', models.CharField(max_length=20)),
                ('address', models.TextField(help_text='Format: Street, City, State/Province, Postal Code, Country')),
                ('company_type', models.CharField(max_length=100)),
                ('registration_number', models.CharField(max_length=100)),
                ('tax_identification_number', models.CharField(max_length=100)),
                ('industry_type', models.CharField(max_length=100)),
                ('date_of_establishment', models.DateField()),
                ('number_of_employees', models.IntegerField()),
                ('business_hours', models.CharField(max_length=100)),
                ('website_url', models.URLField()),
                ('social_media_links', models.TextField(blank=True, help_text='Format: Facebook, Twitter, LinkedIn, Instagram', null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='media/logos/')),
                ('additional_notes', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message_body', models.TextField()),
                ('send_time', models.DateTimeField(auto_now_add=True)),
                ('email_template', models.CharField(blank=True, max_length=255, null=True)),
                ('priority_level', models.CharField(blank=True, max_length=50, null=True)),
                ('cc', models.EmailField(blank=True, max_length=254, null=True)),
                ('bcc', models.EmailField(blank=True, max_length=254, null=True)),
                ('personalization_tags', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_id', models.CharField(max_length=20, unique=True)),
                ('full_name', models.CharField(max_length=100, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('role', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
                ('date_of_creation', models.DateField(auto_now_add=True, null=True)),
                ('last_login_date', models.DateField(blank=True, null=True)),
                ('is_super_admin', models.BooleanField(default=False, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='custom_user_set', related_query_name='user', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='custom_user_set', related_query_name='user', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='attachments/')),
                ('email_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='pos_admin.emaillog')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('owner_name', models.CharField(max_length=100)),
                ('payment_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('credit_card', 'Credit Card'), ('bank_transfer', 'Bank Transfer')], max_length=20)),
                ('transaction_id', models.CharField(max_length=100)),
                ('payment_status', models.CharField(choices=[('paid', 'Paid'), ('pending', 'Pending'), ('failed', 'Failed')], max_length=10)),
                ('notes', models.TextField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pos_admin.company')),
            ],
        ),
    ]
