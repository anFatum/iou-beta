import {SET_PREDICTED_BOX, SET_TRUTH_GROUND_BOX} from "../actionTypes/boundingBoxActionTypes";

export const boundingBoxReducer = (state, action) => {
    const {type} = action || {};
    if (!type) throw new Error('Action type must be defined');
    switch (type) {
        case SET_TRUTH_GROUND_BOX:
            return {...state, truthBox: action.boundingBox}
        case SET_PREDICTED_BOX:
            return {...state, predictedBox: action.boundingBox}
        default:
            return state;
    }
};
