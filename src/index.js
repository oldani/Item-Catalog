import 'bootstrap/dist/css/bootstrap.css';
import React from 'react';
import { render } from 'react-dom';
import App from './App';
import configureStore from './store';

const store = configureStore();

render(
  <App store={store} />,
  document.getElementById('root'),
);
