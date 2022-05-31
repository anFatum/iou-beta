from app.configs import get_config
from app import create_app, socketio


if __name__ == '__main__':
    cfg = get_config("dev")
    app = create_app(cfg)
    socketio.run(app, debug=cfg.DEBUG)
    # app.run(debug=cfg.DEBUG)
