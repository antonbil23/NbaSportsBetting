import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import ToggleMenu from './toggle';
import Home from './pages/Home';
import PDF from './pages/PDF';
import Slides from './pages/Slides'
import NotFound from './pages/NotFound';

import './App.css';

function App() {
    return (
      <Router>
        <ToggleMenu />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/pdf" element={<PDF />} />
          <Route path="/slides" element={<Slides />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </Router>
    );
}

export default App;
