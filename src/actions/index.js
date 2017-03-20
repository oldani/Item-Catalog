export const FETCH_CATEGORY_START = 'FETCH_CATEGORY_START';
export const FETCH_CATEGOTY_ERROR = 'FETCH_CATEGOTY_ERROR';
export const FETCH_CATEGORY_SUCCESS = 'FETCH_CATEGORY_SUCCESS';
export const FETCH_LASTEST_ITEMS_START = 'FETCH_LASTEST_ITEMS_START';
export const FETCH_LASTEST_ITEMS_ERROR = 'FETCH_LASTEST_ITEMS_ERROR';
export const FETCH_LASTEST_ITEMS_SUCCESS = 'FETCH_LASTEST_ITEMS_SUCCESS';
export const FETCH_ITEM_START = 'FETCH_ITEM_START';
export const FETCH_ITEM_ERROR = 'FETCH_ITEM_ERROR';
export const FETCH_ITEM_SUCCESS = 'FETCH_ITEM_SUCCESS';


const requestStart = (actionName) => ({
  type: actionName,
  isFetching: true,
});

const responseSucces = (actionName, data) => ({
  type: actionName,
  isFetching: false,
  entities: data,
});

const responseFail = (actionName, error) => ({
  type: actionName,
  isFetching: false,
  errors: true,
  errorMsg: error,
});

const fetchGet = (dispatch, url, onSuccess, onError) => (
  fetch(url)
    .then(response => {
      if (response.ok) return response.json();
      throw response.error();
    })
    .then(response => dispatch(responseSucces(onSuccess, response)))
    .catch(error => dispatch(responseFail(onError, error)))
);

export const fetchCategories = (dispatch) => {
  dispatch(requestStart(FETCH_CATEGORY_START));
  return fetchGet(dispatch,
    'api/categories',
    FETCH_CATEGORY_SUCCESS,
    FETCH_CATEGOTY_ERROR);
};


export const fetchLatestItems = (dispatch) => {
  dispatch(requestStart(FETCH_LASTEST_ITEMS_START));
  return fetchGet(dispatch,
    'api/items?sort_by=created&order=desc',
    FETCH_LASTEST_ITEMS_SUCCESS,
    FETCH_LASTEST_ITEMS_ERROR);
};

export const fetchItem = (itemId) => (
  dispatch => {
    dispatch(requestStart(FETCH_ITEM_START));

    return fetchGet(dispatch,
      `api/items/${itemId}`,
      FETCH_ITEM_SUCCESS,
      FETCH_ITEM_ERROR);
  }
);
