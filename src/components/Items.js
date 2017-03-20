import React from 'react';
import { connect } from 'react-redux';
import { fetchLatestItems } from '../actions';

class Items extends React.Component {
  componentWillMount() {
    this.props.dispatch(fetchLatestItems);
  }
  render() {
    const { entities } = this.props.latestItems;
    return (
      <div>
        <ul>
          {entities && entities.map(item => (
            <li key={item.id}>
              <a href="#">{item.name}</a>
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

Items.propTypes = {
  dispatch: React.PropTypes.func.isRequired,
  latestItems: React.PropTypes.object.isRequired,
};

const mapStateToProps = (state) => ({
  latestItems: state.items.latest,
});

Items = connect(mapStateToProps)(Items);


export default Items;
