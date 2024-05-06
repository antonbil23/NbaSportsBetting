import React, { useState } from 'react';
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
                        <li><a href="#pdf">PDF</a></li>
                        <li><a href="#slides">Slides</a></li>
                        <li><a href="#code">Code</a></li>
                        <li><a href="#history">History</a></li>
                    </ul>
                </nav>
            </div>
            {/* <div className={`main-content ${isOpen ? 'shifted' : ''}`}>
                <h1>Main Content</h1>
                {/* other content */}
             
        </div>
    );
}

export default ToggleMenu;
