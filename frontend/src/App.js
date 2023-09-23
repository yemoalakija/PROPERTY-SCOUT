import styles from "./App.module.css";
import NavBar from "./components/NavBar";
import { Routes, Route } from "react-router-dom";
import { Container } from "react-bootstrap";

function App() {
  return (
    <div className={styles.App}>
      <NavBar />
        <Container className={styles.Main}>
          <Routes>
            <Route exact path="/" element={<h1>Home Page React Bootstrap</h1>} />
            <Route exact path="/signin" element={<h1>Sign In Page React Bootstrap</h1>} />
            <Route exact path="/signup" element={<h1>Sign Up Page React Bootstrap</h1>} />
            <Route path="*" element={<PageNotFound />} />
          </Routes>
        </Container>
    </div>
  );
}

function PageNotFound() {
  return (
    <div>
      <h1>404: Page not found!</h1>
    </div>
  )
};

export default App;
