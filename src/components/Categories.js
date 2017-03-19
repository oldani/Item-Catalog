import React from 'react';
import { connect } from 'react-redux';
import { fetchCategories } from '../actions';

class Categories extends React.Component {
  componentWillMount() {
    this.props.dispatch(fetchCategories);
  }
  render() {
    const { entities } = this.props.categories;
    return (
      <div>
        <ul>
          { entities && entities.map((item) => (
            <li key={item.id}>
              <a href={`categories/${item.id}`}>{item.name}</a>
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

Categories.propTypes = {
  categories: React.PropTypes.object.isRequired,
  dispatch: React.PropTypes.func.isRequired,
};

const mapStateToProps = (state) => ({
  categories: state.categories,
});

Categories = connect(mapStateToProps)(Categories);

export default Categories;
