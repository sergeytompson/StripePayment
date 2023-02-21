from django.core.exceptions import ValidationError


def is_positive(value):
    if value <= 0:
        raise ValidationError('Введите положительное число')
