import React, { useEffect, useState } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchWorkouts = async () => {
      try {
        const response = await fetch('https://organic-halibut-w9x4v57r4hgrgg-8000.app.github.dev/api/workouts/');
        if (!response.ok) {
          throw new Error(`Erro HTTP: ${response.status}`);
        }
        const data = await response.json();
        setWorkouts(data.results || data);
        setLoading(false);
      } catch (error) {
        setError(`Falha ao carregar treinos: ${error.message}`);
        setLoading(false);
      }
    };

    fetchWorkouts();
  }, []);

  if (loading) return <div className="text-center mt-5"><div className="spinner-border text-primary" role="status"><span className="visually-hidden">Carregando...</span></div></div>;
  if (error) return <div className="alert alert-danger mt-3">{error}</div>;

  // Função para mostrar nível de dificuldade
  const getDifficultyLabel = (level) => {
    switch(level) {
      case 1: return <span className="badge bg-success">Fácil</span>;
      case 2: return <span className="badge bg-warning text-dark">Médio</span>;
      case 3: return <span className="badge bg-danger">Difícil</span>;
      default: return <span className="badge bg-secondary">Não definido</span>;
    }
  };

  // Função para formatar duração
  const formatDuration = (seconds) => {
    if (!seconds) return 'N/A';
    
    // Se segundos já for uma string formatada, retorná-la
    if (typeof seconds === 'string' && seconds.includes(':')) return seconds;
    
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    
    if (hours > 0) {
      return `${hours}h ${minutes}min`;
    } else {
      return `${minutes}min`;
    }
  };

  return (
    <div className="workouts-container">
      <h1 className="mb-4 text-center">Treinos</h1>
      {workouts.length === 0 ? (
        <p className="text-center">Nenhum treino encontrado.</p>
      ) : (
        <div className="row">
          {workouts.map((workout) => (
            <div key={workout._id} className="col-md-6 col-lg-4 mb-4">
              <div className="card h-100">
                <div className="card-header">
                  <h5 className="card-title">{workout.name}</h5>
                  {getDifficultyLabel(workout.difficulty)}
                </div>
                <div className="card-body">
                  <h6 className="card-subtitle mb-2 text-muted">
                    Tipo: {workout.activity_type}
                  </h6>
                  <p className="card-text">{workout.description}</p>
                  <p className="card-text">
                    <strong>Duração:</strong> {formatDuration(workout.duration)}
                  </p>
                </div>
                <div className="card-footer text-muted">
                  Criado em: {new Date(workout.created_at).toLocaleDateString()}
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Workouts;
