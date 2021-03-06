import {Col, Container, Row} from "react-bootstrap";
import {useState} from "react";
import BoundingBoxForm from "../components/boundingBoxForm";
import ToastNotification from "../components/toastNotification";
import Canvas from "../components/canvas";
function HomePage() {

    const [currentIou, setCurrentIou] = useState(undefined);

    return (
        <>
            <ToastNotification/>
            <Container>
                <Row className="justify-content-md-center py-4">
                    <Col xs lg="4" md="auto" className={"text-center"}>
                        <h2>
                            Home page
                        </h2>
                    </Col>
                </Row>

                <Row>
                    <Col xs={4}>
                        <BoundingBoxForm/>
                    </Col>
                    <Col xs={8}>
                        <Canvas style={{
                            width: "100%",
                            height: "100vh"
                        }}/>
                    </Col>
                </Row>

            </Container>
        </>
    );
}

export default HomePage;
