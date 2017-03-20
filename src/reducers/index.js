import { combineReducers } from 'redux';
import {
  FETCH_CATEGORY_START,
  FETCH_CATEGORY_SUCCESS,
  FETCH_CATEGORY_ERROR,
  FETCH_LASTEST_ITEMS_START,
  FETCH_LASTEST_ITEMS_ERROR,
  FETCH_LASTEST_ITEMS_SUCCESS,
  FETCH_ITEM_START,
  FETCH_ITEM_ERROR,
  FETCH_ITEM_SUCCESS,
} from '../actions';

const categories = (state = {
  isFetching: false,
  errors: false,
  errorMsg: '',
  entities: [],
}, action) => {
  switch (action.type) {
    case FETCH_CATEGORY_START:
      return {
        ...state,
        isFetching: action.isFetching,
      };
    case FETCH_CATEGORY_SUCCESS:
      return {
        ...state,
        isFetching: action.isFetching,
        entities: action.entities,
      };
    case FETCH_CATEGORY_ERROR:
      return {
        ...state,
        errors: action.error,
        errorMsg: action.errorMsg,
      };
    default:
      return state;
  }
};

const latest = (state = {
  isFetching: false,
  errors: false,
  errorMsg: '',
  entities: [],
}, action) => {
  switch (action.type) {
    case FETCH_LASTEST_ITEMS_START:
      return {
        ...state,
        isFetching: action.isFetching,
      };
    case FETCH_LASTEST_ITEMS_SUCCESS:
      return {
        ...state,
        isFetching: action.isFetching,
        entities: action.entities,
      };
    case FETCH_LASTEST_ITEMS_ERROR:
      return {
        ...state,
        errors: action.error,
        errorMsg: action.errorMsg,
      };
    default:
      return state;
  }
};

const entity = (state = {
  isFetching: false,
  errors: false,
  errorMsg: '',
  data: {},
}, action) => {
  switch (action.type) {
    case FETCH_ITEM_START:
      return {
        ...state,
        isFetching: action.isFetching,
      };
    case FETCH_ITEM_SUCCESS:
      return {
        ...state,
        isFetching: action.isFetching,
        data: action.entities,
      };
    case FETCH_ITEM_ERROR:
      return {
        ...state,
        errors: action.error,
        errorMsg: action.errorMsg,
      };
    default:
      return state;
  }
};

const items = combineReducers({
  latest,
  entity,
});

const rootReducer = combineReducers({
  categories,
  items,
});

export default rootReducer;
