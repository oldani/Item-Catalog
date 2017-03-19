import React from 'react';
import './App.css';
import { Navbar, Categories, Items } from './components';

const App = () => (
  <main>
    <Navbar />
    <section className="container">
      <Categories />
      <Items />
    </section>
  </main>
);

export default App;
