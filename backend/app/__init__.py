import os

import werkzeug
from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO

werkzeug.cached_property = werkzeug.utils.cached_property
werkzeug.wrappers.BaseResponse = werkzeug.Response
import flask.scaffold

flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func

from flask_restplus import Api
from flask_restful import Api as RestfulApi

from app.configs import Configs
from app.core.utils.logger import get_logger, log_request

logger = get_logger()
socketio = SocketIO()


def create_app(app_configs):
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": app_configs.CORS_ORIGINS,
                                 "expose_headers": ["Origin", "X-Requested-With", "Content-Type", "Accept"],
                                 "supports_credentials": True}})

    @app.after_request
    def log_incoming_request(response):
        log_request(app, response)
        return response

    app.config.from_object(app_configs)
    app.secret_key = app_configs.SECRET_KEY
    app.config['RESTPLUS_MASK_SWAGGER'] = False
    restful_api = RestfulApi(app)

    api = Api(app, doc='/docs')
    socketio.init_app(app)

    from app.iou.controllers.iou_controller import api as iou_api
    from app.iou.controllers.iou_controller import SocketIOU
    api.add_namespace(iou_api)
    restful_api.add_resource(SocketIOU, "/iou")

    return app
