import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import ToggleMenu from './toggle';
import NotFound from './pages/NotFound';

import './App.css';

function App() {
    return (
      <Router>
        <Routes>
          <Route path="/" element={<Navigate to="/home" />} />
          <Route path="/*" element={<ToggleMenu/>} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </Router>
    );
}

export default App;
