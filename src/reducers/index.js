import { combineReducers } from 'redux';
import {
  FETCH_CATEGORIES_START,
  FETCH_CATEGORIES_SUCCESS,
  FETCH_CATEGORIES_ERROR,
} from '../actions';

const categories = (state = {
  isFetching: false,
  errors: false,
  entities: [],
}, action) => {
  switch (action.type) {
    case FETCH_CATEGORIES_START:
      return {
        ...state,
        isFetching: action.isFetching,
      };
    case FETCH_CATEGORIES_SUCCESS:
      return {
        ...state,
        isFetching: action.isFetching,
        entities: action.entities,
      };
    case FETCH_CATEGORIES_ERROR:
      return {
        ...state,
        errors: action.error,
        errorMsg: action.errorMsg,
      };
    default:
      return state;
  }
};

const rootReducer = combineReducers({
  categories,
});

export default rootReducer;
