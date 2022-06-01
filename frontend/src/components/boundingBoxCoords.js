import {Col, Container, Row, Form} from "react-bootstrap";
import {useState, useEffect, useContext} from "react";
import {StoreContext} from "../store";
import {setBoundingBox} from "../store/actions/boundingBoxActions"

const initBox = {
    left: 0,
    top: 0,
    right: 0,
    bottom: 0
}

const BoundingBoxCoords = (props) => {

    const {boxType} = props;
    const [currentIou, setCurrentIou] = useState(initBox);
    const {dispatch} = useContext(StoreContext);

    useEffect(() => {
        dispatch(setBoundingBox(currentIou, boxType));
    }, [currentIou])

    return (
        <>
            <Container>
                <Row>
                    <Col>
                        <Form.Group className="mb-3" controlId={`${boxType}.left`}>
                            <Form.Label>Left</Form.Label>
                            <Form.Control type="number" step="0.01"
                                          min={0} value={currentIou.left}
                                          onChange={e => setCurrentIou({
                                              ...currentIou,
                                              left: Number(e.target.value)
                                          })}
                            />
                        </Form.Group>
                    </Col>
                    <Col>
                        <Form.Group className="mb-3" controlId={`${boxType}.top`}>
                            <Form.Label>Top</Form.Label>
                            <Form.Control type="number" step="0.01" min={0} value={currentIou.top}
                                          onChange={e => setCurrentIou({
                                              ...currentIou,
                                              top: Number(e.target.value)
                                          })}/>
                        </Form.Group>
                    </Col>
                </Row>
                <Row>
                    <Col>
                        <Form.Group className="mb-3" controlId={`${boxType}.right`}>
                            <Form.Label>Right</Form.Label>
                            <Form.Control type="number" step="0.01" min={0} value={currentIou.right}
                                          onChange={e => setCurrentIou({
                                              ...currentIou,
                                              right: Number(e.target.value)
                                          })}
                            />
                        </Form.Group>
                    </Col>
                    <Col>
                        <Form.Group className="mb-3" controlId={`${boxType}.bottom`}>
                            <Form.Label>Bottom</Form.Label>
                            <Form.Control type="number" step="0.01" min={0} value={currentIou.bottom}
                                          onChange={e => setCurrentIou({
                                              ...currentIou,
                                              bottom: Number(e.target.value)
                                          })}
                            />
                        </Form.Group>
                    </Col>
                </Row>
            </Container>
        </>
    );
}

export default BoundingBoxCoords;
