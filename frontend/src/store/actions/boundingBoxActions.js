import {SET_TRUTH_GROUND_BOX, SET_PREDICTED_BOX} from "../actionTypes/boundingBoxActionTypes";

export const setBoundingBox = (boundingBox, type) => {
    let boxType;
    switch (type) {
        case "truth":
            boxType = SET_TRUTH_GROUND_BOX;
            break;
        case "predict":
            boxType = SET_PREDICTED_BOX;
            break;
        default:
            throw new Error("Invalid bounding box type!")
    }
    return {
        type: boxType,
        boundingBox
    }
};