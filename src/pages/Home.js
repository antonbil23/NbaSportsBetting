import React from 'react';
import '../App.css';
import logo from '../nba-logo.png';

function Home() {
  return (
    <div className="App">
      <div className="centered-container">
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
            <a className="App-link" href="https://www.linkedin.com/in/rahul-aneja-746ba5207/" target="_blank"> Rahul Aneja</a>, 
            <a className="App-link" href="https://www.linkedin.com/in/gioromruiz/" target="_blank"> Gio Romero-Ruiz</a>, 
            <a className="App-link" href="https://www.linkedin.com/in/antonbilonog/" target="_blank"> Anton Bilonog</a>
            </div>
      </div>

      <header className="App-header">
        <p>
          <code>Further Content...</code> 
        </p>
        
      </header>


    </div>
  );
}

export default Home;
