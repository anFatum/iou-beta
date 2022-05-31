import React, {useReducer} from 'react';
import {rootReducer} from './store/reducers/rootReducer';
import {StoreContext} from "./store";

import AppRoutes from "./Routes";

function App() {
    const [globalState, dispatch] = useReducer(rootReducer, {});
    return (
        <div className="App">
            <StoreContext.Provider value={{globalState, dispatch}}>
                <AppRoutes/>
            </StoreContext.Provider>
        </div>
    );
}

export default App;
