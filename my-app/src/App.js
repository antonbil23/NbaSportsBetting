import React from 'react';
import './App.css';
import logo from './nba-logo.png';
import ToggleMenu from './toggle.js';

function App() {
  return (
    <div className="App">
      <ToggleMenu />
      <div className="Home-header">
        <div>
        <img src={logo} className="NBA-logo" alt="Nba Logostyle" />
        </div>
        <div className="title">
        NBA Sports Betting Prediction Model
        </div>
      </div>
      
      <div className="authors">
                By: 
                <a className="App-link" href="https://www.linkedin.com/in/rahul-aneja-746ba5207/"> Rahul Aneja</a>, 
                <a className="App-link" href="https://www.linkedin.com/in/gioromruiz/"> Gio Romero-Ruiz</a>, 
                <a className="App-link" href="https://www.linkedin.com/in/antonbilonog/"> Anton Bilonog</a>
            </div>

      <header className="App-header">
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>


    </div>
  );
}

export default App;
