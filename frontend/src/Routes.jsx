import * as React from "react";
import {BrowserRouter, Navigate, Route, Routes} from "react-router-dom";
import HomePage from "./pages/HomePage";

const AppRoutes = () => {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/"
                       element={<Navigate to="/home"/>}
                />
                <Route path="/home" element={<HomePage/>}/>
            </Routes>
        </BrowserRouter>
    );
};

export default AppRoutes;