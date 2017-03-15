import React from 'react';


const Navbar = () => (
  <header>
    <nav className="navbar navbar-toggleable-md navbar-light bg-faded justify-content-between">
      <a className="navbar-brand" href="#">Item-Catalog</a>
      <ul className="nav">
        <li className="nav-item">
          <a className="nav-link btn btn-outline-primary" href="#">Sign up</a>
        </li>
        <li className="nav-item">
          <a className="nav-link btn btn-outline-success" href="#">Login</a>
        </li>
      </ul>
    </nav>
  </header>
);


export default Navbar;
