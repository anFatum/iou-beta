from app.core.abc.exceptions import ValidationError
from decimal import Decimal, InvalidOperation


def convert_to_number(x):
    try:
        return Decimal(x)
    except (TypeError, ValueError, InvalidOperation) as e:
        raise ValidationError()
