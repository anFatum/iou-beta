import React, {useContext, useEffect, useRef} from 'react';
import {StoreContext} from "../store";

const Canvas = props => {
    const {globalState, dispatch} = useContext(StoreContext);
    const truthColor = "rgba(166,220,219,0.8)";
    const predictedColor = "rgba(250,87,71,0.8)";
    const intersectColor = "#ffefa5";

    const draw = (canvas) => {
        const context = canvas.getContext('2d')
        const {width, height} = canvas.getBoundingClientRect();
        drawBoundingBoxes(context, width, height);
    }

    const boxesIntersect = (truthBox, predictedBox) => {
        return !(truthBox['left'] >= predictedBox['right'] || truthBox['top'] >= predictedBox['bottom']
            || truthBox['right'] <= predictedBox['left'] || truthBox['bottom'] <= predictedBox['top']);
    }

    const drawBoundingBoxes = (context, width, height) => {
        const {truthBox, predictedBox} = globalState.boundingBoxReducer || {};
        if (truthBox && predictedBox) {
            const mappedTruthBox = mapBoundingBox(truthBox, width, height)
            const mappedPredictedBox = mapBoundingBox(predictedBox, width, height)
            context.clearRect(0, 0, width, height);
            drawBoundingBox(context, mappedTruthBox, truthColor, width, height);
            drawBoundingBox(context, mappedPredictedBox, predictedColor, width, height);
            if (boxesIntersect(mappedTruthBox, mappedPredictedBox)) {
                const intersectBox = {
                    left: Math.max(mappedTruthBox['left'], mappedPredictedBox['left']),
                    top: Math.max(mappedTruthBox['top'], mappedPredictedBox['top']),
                    right: Math.min(mappedTruthBox['right'], mappedPredictedBox['right']),
                    bottom: Math.min(mappedTruthBox['bottom'], mappedPredictedBox['bottom'])
                };
                drawBoundingBox(context, intersectBox, intersectColor);
            }
        }
    }

    const mapBoundingBox = (boxCoords, width, height) => {
        return {
            right: boxCoords['right'] * width,
            left: boxCoords['left'] * width,
            bottom: boxCoords['bottom'] * height,
            top: boxCoords['top'] * height
        };
    }

    const drawBoundingBox = (context, boxCoords, color) => {
        context.beginPath();
        context.fillStyle = color;
        context.rect(boxCoords['left'], boxCoords['top'],
            Math.max(boxCoords['right'] - boxCoords['left'], 0),
            Math.max(boxCoords['bottom'] - boxCoords['top'], 0));
        context.fill();
    }

    const canvasRef = useRef(null);

    const resizeCanvasToDisplaySize = (canvas) => {
        const {width, height} = canvas.getBoundingClientRect()

        if (canvas.width !== width || canvas.height !== height) {
            const {devicePixelRatio: ratio = 1} = window;
            const context = canvas.getContext('2d');
            canvas.width = width * ratio;
            canvas.height = height * ratio;
            context.scale(ratio, ratio);
            return true;
        }

        return false
    }

    useEffect(() => {
        const canvas = canvasRef.current;
        resizeCanvasToDisplaySize(canvas);
        draw(canvas);
    }, [])

    useEffect(() => {
        const canvas = canvasRef.current;
        draw(canvas);
    }, [globalState.boundingBoxReducer?.truthBox, globalState.boundingBoxReducer?.predictedBox])


    return <canvas className={"iouCanvas"} ref={canvasRef} {...props}/>
}

export default Canvas