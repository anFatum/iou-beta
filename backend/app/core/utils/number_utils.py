from decimal import Decimal, InvalidOperation

from app.core.abc.exceptions import ValidationError

ALLOWED_NUMBER_CLASSES = (Decimal, float, int)


def convert_to_number(x, number_class=Decimal):
    """
    Function converts input to be one of allowed number classes.
    Raises ValidationError if the input can't be converted.
    Raises ValueError if number class is not of the allowed ones.
    """
    if not issubclass(number_class, ALLOWED_NUMBER_CLASSES):
        raise ValueError("Wrong number class!")
    try:
        return number_class(x)
    except (TypeError, ValueError, InvalidOperation) as e:
        raise ValidationError(f"{x} is not a number!")
