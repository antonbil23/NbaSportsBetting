import React, { useState } from 'react';
import { Link, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import PDF from './pages/PDF';
import Slides from './pages/Slides';
import NotFound from './pages/NotFound';
import './App.css';

function ToggleMenu() {
    const [isOpen, setIsOpen] = useState(false);

    const toggleMenu = () => {
        setIsOpen(!isOpen);
    };

    return (
        <div className="container">
            <div className="sidebar">
                <div className="hamburger" onClick={toggleMenu}>
                    <div className="line"></div>
                    <div className="line"></div>
                    <div className="line"></div>
                </div>
                <nav className={`menu ${isOpen ? 'open' : ''}`}>
                    <ul>
                        <li><Link to="/" onClick={toggleMenu}>Home</Link></li>
                        <li><Link to="/pdf" onClick={toggleMenu}>PDF</Link></li>
                        <li><Link to="/slides" onClick={toggleMenu}>Slides</Link></li>
                    </ul>
                </nav>
            </div>
            {/* <div className={`main-content ${isOpen ? 'shifted' : ''}`}>
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/pdf" element={<PDF />} />
                    <Route path="/slides" element={<Slides />} />
                    <Route path="*" element={<NotFound />} />
                </Routes>
            </div> */}
        </div>
    );
}

export default ToggleMenu;
