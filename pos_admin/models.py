from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import BaseUserManager
from .validators import validate_alpha, alpha_validator, validate_phone_number_length


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)
class AdminUser(AbstractUser):
    user_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=100, null=True , validators=[alpha_validator])
    phone_number = models.CharField(max_length=15, blank=True, null=True , validators=[validate_phone_number_length])
    role = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    date_of_creation = models.DateField(auto_now_add=True, null=True)
    last_login_date = models.DateField(blank=True, null=True)
    is_super_admin = models.BooleanField(default=False, null = True) 
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Add related_name to avoid clash
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Add related_name to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )
    
    def get_full_name(self):
        return self.full_name

    objects = UserManager()  # Attach the custom manager

# COMPANY
class Company(models.Model):
    name = models.CharField(max_length=255, validators=[alpha_validator])
    # name = models.CharField(max_length=255)
    company_id = models.CharField(max_length=50, unique=True)
    contact_person_name = models.CharField(max_length=255, validators=[alpha_validator])
    # contact_person_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone_number = models.CharField(max_length=20, validators=[validate_phone_number_length])
    # contact_phone_number = models.CharField(max_length=20)
    address = models.TextField(help_text="Format: Street, City, State/Province, Postal Code, Country")
    company_type = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=100)
    tax_identification_number = models.CharField(max_length=100)
    industry_type = models.CharField(max_length=100)
    date_of_establishment = models.DateField()
    number_of_employees = models.IntegerField()
    business_hours = models.CharField(max_length=100)
    website_url = models.URLField()
    social_media_links = models.TextField(help_text="Format: Facebook, Twitter, LinkedIn, Instagram", blank=True, null=True)
    logo = models.ImageField(upload_to='media/logos/', blank=True, null=True)
    additional_notes = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# PAYMENT

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
        # Add other methods as needed
    ]
    
    PAYMENT_STATUS = [
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('failed', 'Failed'),
    ]
    
    payment_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    owner_name = models.CharField(max_length=100)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.company_name} - {self.amount} - {self.payment_status}'
# Email
from django.db import models
from django.db import models

class EmailLog(models.Model):
    user = models.ForeignKey(AdminUser, on_delete=models.CASCADE, related_name='email_logs', null=True)
    recipient = models.EmailField()
    subject = models.CharField(max_length=255, null=True)
    message_body = models.TextField(null=True)
    send_time = models.DateTimeField(auto_now_add=True)
    email_template = models.CharField(max_length=255, blank=True, null=True)
    priority_level = models.CharField(max_length=50, blank=True, null=True)
    cc = models.EmailField(blank=True, null=True)
    bcc = models.EmailField(blank=True, null=True)
    personalization_tags = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.subject

class Attachment(models.Model):
    email_log = models.ForeignKey(EmailLog, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')