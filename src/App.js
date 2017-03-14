import React, { Component } from 'react';
import './App.css';
import { Navbar, Categories, Items } from './components';


class App extends Component {
  render() {
    return (
      <main>
        <Navbar />
        <section className="container">
          <Categories />
          <Items />
        </section>
      </main>
    );
  }
}

export default App;
