from http import HTTPStatus

from flask_restplus import Resource
from flask import request
from app.iou.utils.dto import IOUDto
from app.iou.services.iou import get_iou
from app.core.utils.logger import get_logger
from app.core.utils.number_utils import convert_to_number
from app.configs import Configs
from decimal import Decimal
from app import socketio

api = IOUDto.api
logger = get_logger("app")


@api.route("")
class IOUCalc(Resource):

    @api.doc("open_account",
             responses={
                 HTTPStatus.BAD_REQUEST: "Bad Request"
             },
             body=IOUDto.bounding_boxes_coords_model)
    @api.expect(IOUDto.bounding_boxes_coords_model, validate=True)
    @api.marshal_with(IOUDto.iou_output_model,
                      code=HTTPStatus.OK)
    def post(self):
        """
        Creates an account for a user (if admin role can create account for any user)
        """
        iou = get_iou(request.json)
        decimal_places = convert_to_number(Configs.DECIMAL_PRECISION, number_class=int)
        iou = iou.quantize(Decimal('1.' + ('0' * decimal_places)))
        return {"iou": iou}, HTTPStatus.OK


class SocketIOU(Resource):
    def __init__(self):
        pass

    @socketio.on('my-event')
    def handle_my_custom_event(self, json):
        print('received json: ' + str(json))
