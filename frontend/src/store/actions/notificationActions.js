import {POP_NOTIFICATION, PUSH_NOTIFICATION} from "../actionTypes/notificationActionTypes";

export const enqueueNotification = (notification) => ({
    type: PUSH_NOTIFICATION,
    notification
});

export const dequeueNotification = () => ({
    type: POP_NOTIFICATION
});
