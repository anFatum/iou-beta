import {notificationReducer} from "./notificationReducer";
import {boundingBoxReducer} from "./boundingBoxReducer";

const combineReducers = (slices) => (state, action) =>
    Object.keys(slices).reduce( // use for..in loop, if you prefer it
        (acc, prop) => ({
            ...acc,
            [prop]: slices[prop](acc[prop], action),
        }),
        state
    );

export const rootReducer = combineReducers({notificationReducer, boundingBoxReducer});