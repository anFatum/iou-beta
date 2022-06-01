import {Toast, ToastContainer} from "react-bootstrap";
import React, {useContext} from 'react';
import {StoreContext} from "../store";
import {dequeueNotification} from '../store/actions/notificationActions';

const NotificationStack = () => {
    const {globalState, dispatch} = useContext(StoreContext);

    const notificationConfig = (notification) => {
        switch (notification.notificationType) {
            case "error":
                return {
                    bg: "danger",
                    className: 'text-white',
                    title: "Error occurred"
                }
            case "success":
                return {
                    bg: "success",
                    className: 'text-white',
                    title: "Success!"
                }
            default:
                return {
                    bg: "danger",
                    className: 'text-white'
                }
        }
    }

    return <>
        <ToastContainer className="p-3" position='top-end'>
            {globalState.notificationReducer?.notifications.map((notification, idx) => {
                const config = notificationConfig(notification);
                return <Toast
                    key={idx}
                    className="d-inline-block m-1" bg={config.bg}
                    onClose={() => {
                        dispatch(dequeueNotification());
                    }}
                    autohide={true}
                >
                    <Toast.Header>
                        <strong className="me-auto">{config.title}</strong>
                        <small>Just now</small>
                    </Toast.Header>
                    <Toast.Body className={config.className}>
                        {notification.notificationMessage}
                    </Toast.Body>
                </Toast>
            })}
        </ToastContainer>
    </>
}

export default NotificationStack;