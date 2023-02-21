from typing import Union

from django.core.exceptions import ValidationError


def is_positive(value: Union[int, float]) -> None:
    if value <= 0:
        raise ValidationError("Введите положительное число")
