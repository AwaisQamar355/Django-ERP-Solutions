from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

def validate_alpha(value):
    if not value.replace(" ", "").isalpha():
        raise ValidationError('Field must contain only alphabetic characters.')

alpha_validator = RegexValidator(
    regex=r'^[a-zA-Z ]+$',
    message='Only alphabetic characters are allowed.',
    code='invalid_name'
)

def validate_phone_number_length(value):
    if len(value) != 11:
        raise ValidationError('Phone number must be exactly 11 digits.')

