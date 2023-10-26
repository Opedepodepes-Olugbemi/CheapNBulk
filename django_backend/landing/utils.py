from django.contrib.auth.models import User
import re

PATTERN = r'^(0|\+234)[789][01]\d{8}$'

def international_phone(number: str):
    print(number)
    number = number.lower().strip()
    if number.startswith('0'): 
        return '+234' + number[1:]
    return number

def clean_phone(number:str):
    """Validates number start with +234 or 0, then 10 digits"""
    number_pattern = re.compile(r'^(?:\+234|0)\d{10}$')
    result = number_pattern.match(number)
    if result:
        if number.startswith('0'): 
            return '+234' + number[1:]
        return number
    else:
        raise serializers.ValidationError({'phone': 'Incorrect phone number.'})

def phone_validation(number: str):
    """Checks if a phone number is valid"""
    int_number = international_phone(number)
    if not re.match(PATTERN, int_number):
        return {"is_valid":False, "message": "Invalid Phone number"}
    try:
        existing_user = User.objects.get(username=int_number)
    except User.DoesNotExist:
        existing_user = None

    if existing_user is not None:
        return {"is_valid":False, "message": "Phone number already registered"}
    return {"is_valid":True, "message": "Valid Phone number", "phone": int_number}