
import React from 'react';
import { Routes, Route } from "react-router-dom";
import { Container } from "react-bootstrap";
import styles from "../App.module.css";
import NavBar from "../components/NavBar";
import PageNotFound from "../components/PageNotFound";

const Layout = (props) => {
    return (
      <div className={styles.App}>
        <NavBar />
        <Container className={styles.Main}>
          {props.children}
          <Routes>
            <Route
              exact
              path="/"
              element={<h1>Home</h1>}
            />
            <Route
              exact
              path="/about"
              element={<h1>About</h1>}
            />
            <Route
              exact
              path="/contact"
              element={<h1>Contact</h1>}
            />
            <Route
              exact
              path="/listings"
              element={<h1>Listings</h1>}
            />
            <Route
              exact
              path="/listing/:id"
              element={<h1>Listing ID</h1>}
            />
            <Route
              exact
              path="/signin"
              element={<h1>Sign In</h1>}
            />
            <Route
              exact
              path="/signup"
              element={<h1>Sign Up</h1>}
            />
            <Route path="*" element={<PageNotFound />} />
          </Routes>
        </Container>
      </div>
    );
}

export default Layout;
