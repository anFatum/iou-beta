from app.core.abc.exceptions import ValidationError
from decimal import Decimal, InvalidOperation


def convert_to_number(x, number_class=Decimal):
    if not issubclass(number_class, (Decimal, float, int)):
        raise ValueError("Wrong number class!")
    try:
        return number_class(x)
    except (TypeError, ValueError, InvalidOperation) as e:
        raise ValidationError(f"{x} is not a number!")
