import {POP_NOTIFICATION, PUSH_NOTIFICATION} from "../actionTypes/notificationActionTypes";

export const notificationReducer = (state, action) => {
    const {type} = action || {};
    if (!type) throw new Error('Action type must be defined');
    let notifications = state?.notifications || [];
    switch (type) {
        case PUSH_NOTIFICATION:
            notifications.push(action.notification);
            return {...state, notifications}
        case POP_NOTIFICATION:
            return {...state, notifications: notifications.slice(1)}
        default:
            return state;
    }
};
