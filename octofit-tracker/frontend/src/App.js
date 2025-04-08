import React from 'react';import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';import './App.css';// Importação dos componentesimport Activities from './components/Activities';import Leaderboard from './components/Leaderboard';import Teams from './components/Teams';import Users from './components/Users';import Workouts from './components/Workouts';function App() {  return (    <Router>      <div className="container">        <nav className="navbar navbar-expand-lg navbar-light bg-light">          <div className="container-fluid">            <Link className="navbar-brand" to="/">OctoFit Tracker</Link>            <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">              <span className="navbar-toggler-icon"></span>            </button>            <div className="collapse navbar-collapse" id="navbarNav">              <ul className="navbar-nav">                <li className="nav-item">                  <Link className="nav-link" to="/activities">Atividades</Link>                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/leaderboard">Classificação</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/teams">Equipes</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/users">Usuários</Link>
                </li>
                <li className="nav-item">
                  <Link className="nav-link" to="/workouts">Treinos</Link>
                </li>
              </ul>
            </div>
          </div>
        </nav>
        <div className="mt-4">
          <Routes>
            <Route path="/activities" element={<Activities />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/teams" element={<Teams />} />
            <Route path="/users" element={<Users />} />
            <Route path="/workouts" element={<Workouts />} />
            <Route path="/" element={
              <div className="text-center">
                <h1>Bem-vindo ao OctoFit Tracker</h1>
                <p className="lead">Aplicativo de fitness para as escolas de Merington</p>
                <img 
                  src="/logo512.png" 
                  alt="OctoFit Logo" 
                  style={{ maxWidth: '300px', marginTop: '20px' }}
                  className="img-fluid"
                />
              </div>
            } />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
