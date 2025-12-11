from django.core.exceptions import ValidationError
import re

def validate_english_username(value):
    if not re.match(r'^[A-Za-z0-9_]+$', value):
        raise ValidationError("Ім'я користувача може містити тільки англійські літери, цифри та _.")
