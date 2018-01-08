import React from 'react';
import ReactDOM from 'react-dom';
import { createStore } from 'redux';
import { Provider } from 'react-redux';
import App from './components/App';
import registerServiceWorker from './registerServiceWorker';
import './index.css';
import './App.css';
import {heroReducer} from "./reducers/heroReducer";

const initialState = {
    hero: {
        id: 0,
        name: 'windstorm'
    }
};

const store = createStore(heroReducer, initialState);

ReactDOM.render(
    <Provider store={store}>
        <App />
    </Provider>,
    document.getElementById('root')
);

registerServiceWorker();
