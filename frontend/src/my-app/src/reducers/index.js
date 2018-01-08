import {combineReducers} from 'redux';
import heroReducer from './heroReducer';

const heroApp = combineReducers({
    heroReducer
});

export default heroApp;
