import {Form, Button} from "react-bootstrap";
import BoundingBoxCoords from "./boundingBoxCoords";
import {enqueueNotification} from "../store/actions/notificationActions";
import getAxiosClient from "../utils/axiosClient";
import {useState, useContext} from "react";
import {StoreContext} from "../store";


function BoundingBoxForm() {
    const [isLoading, setIsLoading] = useState(false);
    const [currentIOU, setCurrentIOU] = useState(0);
    const {globalState, dispatch} = useContext(StoreContext);

    const handleCalcIOU = async () => {
        const axios = getAxiosClient();
        setIsLoading(true);
        try {
            const response = await axios.post("iou", {
                ground_truth: globalState.boundingBoxReducer.truthBox,
                predicted: globalState.boundingBoxReducer.predictedBox
            });
            setCurrentIOU(response.data.iou);
        } catch (err) {
            dispatch(enqueueNotification({
                notificationType: "error",
                notificationMessage: err.response?.data?.message || "An error occurred"
            }))
        }
        setIsLoading(false);
    }

    return (
        <>
            <Form>
                <h5>Predicted</h5>
                <BoundingBoxCoords boxType={'predict'}/>
                <h5>Truth ground</h5>
                <BoundingBoxCoords boxType={'truth'}/>
                <Button
                    onClick={() => handleCalcIOU()}
                >Calc IOU</Button>
                <h5 className={'pt-3'}>Calculated IOU: {currentIOU}</h5>
            </Form>
        </>
    );
}

export default BoundingBoxForm;
