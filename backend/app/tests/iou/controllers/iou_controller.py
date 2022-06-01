import json
from http import HTTPStatus

API_ENDPOINT = '/iou'


def test_ok_status(client):
    json_data = {
        "ground_truth": {
            "left": 0.1,
            "top": 0.15,
            "right": 0.2,
            "bottom": 0.55
        },
        "predicted": {
            "left": 0.04,
            "top": 0.25,
            "right": 0.22,
            "bottom": 0.41
        }
    }
    rv = client.post(API_ENDPOINT,
                     data=json.dumps(json_data),
                     content_type='application/json')
    assert rv.status_code == HTTPStatus.OK
    assert "iou" in rv.json


def test_missing_data(client):
    json_data = {}
    rv = client.post(API_ENDPOINT,
                     data=json.dumps(json_data),
                     content_type='application/json')
    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert "errors" in rv.json


def test_invalid_coordinates(client):
    example_string = 's'
    json_data = {
        "ground_truth": {
            "left": example_string,
            "top": example_string,
            "right": example_string,
            "bottom": example_string
        },
        "predicted": {
            "left": example_string,
            "top": example_string,
            "right": example_string,
            "bottom": example_string
        }
    }
    rv = client.post(API_ENDPOINT,
                     data=json.dumps(json_data),
                     content_type='application/json')
    assert rv.status_code == HTTPStatus.BAD_REQUEST
    assert "errors" in rv.json
