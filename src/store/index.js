import { createStore, applyMiddleware } from 'redux';
import createLogger from 'redux-logger';
import rootReducer from '../reducers';

const configureStore = () => {
  const milddlewares = [];
  if (process.env.NODE_ENV !== 'production') {
    milddlewares.push(createLogger());
  }
  const store = createStore(rootReducer, applyMiddleware(...milddlewares));

  return store;
};


export default configureStore;
