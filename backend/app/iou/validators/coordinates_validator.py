from app.core.utils.number_utils import convert_to_number
from app.core.abc.exceptions import ValidationError


class CoordinatesValidator:
    instance = None

    def validate(self, bounding_box: dict) -> dict:
        """
        Validates if the coordinates are valid for calculation the IOU
        All coordinates should be a number, greater than zero and
        be valid box coordinate (left is smaller than right and top smaller than bottom)
        Raises a Validation error otherwise
        """
        if not isinstance(bounding_box, dict):
            raise ValidationError()
        bounding_box = self._validate_coords_numbers(bounding_box)
        self._validate_valid_box(bounding_box)
        return bounding_box

    def _validate_coords_numbers(self, bounding_box: dict) -> dict:
        try:
            bounding_box['left'] = convert_to_number(bounding_box.get('left'))
            bounding_box['top'] = convert_to_number(bounding_box.get('top'))
            bounding_box['right'] = convert_to_number(bounding_box.get('right'))
            bounding_box['bottom'] = convert_to_number(bounding_box.get('bottom'))
        except ValidationError:
            raise ValidationError("Coordinates should be a number!")
        return bounding_box

    def _validate_valid_box(self, bounding_box: dict) -> None:
        if not bounding_box['left'] < bounding_box['right'] or not bounding_box['top'] < bounding_box['bottom']:
            raise ValidationError("Left coordinate should be less than right, and top be less than bottom!")

    def _validate_coords_greater_zero(self, bounding_box: dict) -> None:
        for coord in bounding_box.values():
            if not coord > 0:
                raise ValidationError("Coordinates should be greater than zero!")
