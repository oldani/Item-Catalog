export const FETCH_CATEGORIES_START = 'FETCH_START';
export const FETCH_CATEGORIES_ERROR = 'FETCH_ERROR';
export const FETCH_CATEGORIES_SUCCESS = 'FETCH_SUCCESS';


const requestCategories = () => ({
  type: FETCH_CATEGORIES_START,
  isFetching: true,
});

const responseCategories = (data) => ({
  type: FETCH_CATEGORIES_SUCCESS,
  isFetching: false,
  entities: data,
});

const failCategories = (error) => ({
  type: FETCH_CATEGORIES_ERROR,
  isFetching: false,
  errors: true,
  errorMsg: error,
});

export const fetchCategories = (dispatch) => {
  dispatch(requestCategories());

  return fetch('api/categories')
    .then(response => {
      if (response.ok) return response.json();
      throw response.error();
    })
    .then(response => dispatch(responseCategories(response)))
    .catch(error => dispatch(failCategories(error)));
};

