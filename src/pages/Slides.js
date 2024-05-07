import React from 'react';
import ToggleMenu from '../toggle.js';
import '../App.css';

function Slides() {
    return (
    <div className="App">
        {/* <ToggleMenu /> */}
        
        <div className="Home-header">Slides</div>

        <object className="pdf" 
            data="./presentation.pdf" 
            width="800" 
            height="500">
            This browser does not support PDFs. Please download the PDF to view it: 
        <a href="/presentation.pdf">Download PDF</a>.
        </object>
    </div>
    );
}

export default Slides;
