from http import HTTPStatus

from werkzeug.exceptions import abort
from decimal import Decimal
from app.core.abc.exceptions import ValidationError
from app.core.utils.number_utils import convert_to_number
from app.iou.validators.coordinates_validator import CoordinatesValidator


def calc_iou(bb1, bb2):
    """
    Calculate the Intersection over Union (IoU) of two bounding boxes.

    Parameters
    ----------
    bb1 : dict
        Keys: {'left', 'right', 'top', 'bottom'}
        The (left, top) position is at the top left corner,
        the (right, bottom) position is at the bottom right corner
    bb2 : dict
        Keys: {'left', 'right', 'top', 'bottom'}
        The (left, top) position is at the top left corner,
        the (right, bottom) position is at the bottom right corner

    Returns
    -------
    float
        in [0, 1]
    """

    # determine the coordinates of the intersection rectangle
    x_left = max(bb1['left'], bb2['left'])
    y_top = max(bb1['top'], bb2['top'])
    x_right = min(bb1['right'], bb2['right'])
    y_bottom = min(bb1['bottom'], bb2['bottom'])

    if x_right < x_left or y_bottom < y_top:
        return 0.0

    # The intersection of two axis-aligned bounding boxes is always an
    # axis-aligned bounding box
    intersection_area = (x_right - x_left) * (y_bottom - y_top)

    # compute the area of both AABBs
    bb1_area = (bb1['right'] - bb1['left']) * (bb1['bottom'] - bb1['top'])
    bb2_area = (bb2['right'] - bb2['left']) * (bb2['bottom'] - bb2['top'])

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the interesection area
    iou = intersection_area / convert_to_number(bb1_area + bb2_area - intersection_area)
    return iou


def get_iou(data: dict) -> Decimal:
    """
    Validates the input for IOU - see CoordinatesValidator for details
    Aborts with BAD REQUEST if hasn't passed the validation

    Parameters
    ----------
    data : dict
        Keys: {'ground_truth', 'predicted'}
        Both are dicts with coordinates:
        Keys: {'left', 'right', 'top', 'bottom'}
        The (left, top) position is at the top left corner,
        the (right, bottom) position is at the bottom right corner

    Returns
    -------
    float
        in [0, 1]
    """
    try:
        bb1 = CoordinatesValidator().validate(data.get("ground_truth"))
        bb2 = CoordinatesValidator().validate(data.get("predicted"))
        return convert_to_number(calc_iou(bb1, bb2))
    except ValidationError as e:
        abort(HTTPStatus.BAD_REQUEST, str(e))
