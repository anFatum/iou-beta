from decimal import Decimal
from app.core.utils.number_utils import convert_to_number
import pytest
from app.core.abc.exceptions import ValidationError


@pytest.mark.parametrize("num_str,num_class", [("5", int), ("2.4", Decimal), ("6.9", float)])
def test_convert_valid_number(num_str, num_class):
    output = convert_to_number(num_str, num_class)
    assert isinstance(output, num_class)


def test_convert_invalid_number():
    with pytest.raises(ValidationError):
        convert_to_number("test1")


def test_convert_invalid_number_class():
    with pytest.raises(ValueError):
        convert_to_number("3.3", bytes)
