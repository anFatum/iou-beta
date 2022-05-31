from flask_restplus import Namespace, fields


class IOUDto:
    api = Namespace("IOU API", path="/iou", description="Account related operations")
    coordinates_model = api.model("Coordinates", {
        "left": fields.Float(required=True),
        "top": fields.Float(required=True),
        "right": fields.Float(required=True),
        "bottom": fields.Float(required=True)
    })
    bounding_boxes_coords_model = api.model("BoundingBoxes", {
        "ground_truth": fields.Nested(coordinates_model, required=True),
        "predicted": fields.Nested(coordinates_model, required=True)
    })
    iou_output_model = api.model("IOUModel", {
        "iou": fields.String()
    })
