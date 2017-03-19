import { createStore, applyMiddleware } from 'redux';
import createLogger from 'redux-logger';
import thunkMiddleware from 'redux-thunk';
import rootReducer from '../reducers';

const configureStore = () => {
  const milddlewares = [thunkMiddleware];
  if (process.env.NODE_ENV !== 'production') {
    milddlewares.push(createLogger());
  }
  const store = createStore(rootReducer, applyMiddleware(...milddlewares));

  return store;
};


export default configureStore;
