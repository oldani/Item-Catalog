import React from 'react';


export const Navbar = () => {
  return (
    <header>
      <nav className="navbar navbar-toggleable-md navbar-light bg-faded">
        <a className="navbar-brand" href="#">Item-Catalog</a>
        <ul className="navbar-nav">
          <li className="nav-item active">
            <a className="nav-link" href="#">Home</a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="#">Sign up</a>
          </li>
          <li className="nav-item">
            <a className="nav-link" href="#">Login</a>
          </li>
        </ul>
      </nav>
    </header>
  );
};
