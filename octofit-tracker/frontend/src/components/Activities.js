import React, { useEffect, useState } from 'react';

function Activities() {
  const [activities, setActivities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchActivities = async () => {
      try {
        const response = await fetch('https://organic-halibut-w9x4v57r4hgrgg-8000.app.github.dev/api/activities/');
        if (!response.ok) {
          throw new Error(`Erro HTTP: ${response.status}`);
        }
        const data = await response.json();
        setActivities(data.results || data);
        setLoading(false);
      } catch (error) {
        setError(`Falha ao carregar atividades: ${error.message}`);
        setLoading(false);
      }
    };

    fetchActivities();
  }, []);

  if (loading) return <div className="text-center mt-5"><div className="spinner-border text-primary" role="status"><span className="visually-hidden">Carregando...</span></div></div>;
  if (error) return <div className="alert alert-danger mt-3">{error}</div>;

  return (
    <div className="activities-container">
      <h1 className="mb-4 text-center">Atividades</h1>
      {activities.length === 0 ? (
        <p className="text-center">Nenhuma atividade encontrada.</p>
      ) : (
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead className="table-dark">
              <tr>
                <th>Usuário</th>
                <th>Tipo</th>
                <th>Duração</th>
                <th>Distância</th>
                <th>Calorias</th>
                <th>Notas</th>
                <th>Data</th>
              </tr>
            </thead>
            <tbody>
              {activities.map((activity) => (
                <tr key={activity._id}>
                  <td>{activity.user_details?.username || 'N/A'}</td>
                  <td>{activity.activity_type}</td>
                  <td>{formatDuration(activity.duration)}</td>
                  <td>{activity.distance ? `${activity.distance} km` : 'N/A'}</td>
                  <td>{activity.calories || 'N/A'}</td>
                  <td>{activity.notes || 'N/A'}</td>
                  <td>{new Date(activity.created_at).toLocaleDateString()}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

// Função auxiliar para formatação da duração
function formatDuration(seconds) {
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
}

export default Activities;
