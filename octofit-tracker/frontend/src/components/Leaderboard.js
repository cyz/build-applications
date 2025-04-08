import React, { useEffect, useState } from 'react';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      try {
        const response = await fetch('https://organic-halibut-w9x4v57r4hgrgg-8000.app.github.dev/api/leaderboard/');
        if (!response.ok) {
          throw new Error(`Erro HTTP: ${response.status}`);
        }
        const data = await response.json();
        setLeaderboard(data.results || data);
        setLoading(false);
      } catch (error) {
        setError(`Falha ao carregar classificação: ${error.message}`);
        setLoading(false);
      }
    };

    fetchLeaderboard();
  }, []);

  if (loading) return <div className="text-center mt-5"><div className="spinner-border text-primary" role="status"><span className="visually-hidden">Carregando...</span></div></div>;
  if (error) return <div className="alert alert-danger mt-3">{error}</div>;

  return (
    <div className="leaderboard-container">
      <h1 className="mb-4 text-center">Classificação</h1>
      {leaderboard.length === 0 ? (
        <p className="text-center">Nenhuma classificação encontrada.</p>
      ) : (
        <div className="table-responsive">
          <table className="table table-striped table-hover">
            <thead className="table-dark">
              <tr>
                <th>Posição</th>
                <th>Usuário</th>
                <th>Pontuação</th>
                <th>Semana</th>
                <th>Ano</th>
              </tr>
            </thead>
            <tbody>
              {leaderboard
                .sort((a, b) => b.score - a.score)
                .map((entry, index) => (
                  <tr key={entry._id}>
                    <td>{index + 1}</td>
                    <td>{entry.user_details?.username || 'N/A'}</td>
                    <td>{entry.score}</td>
                    <td>{entry.week}</td>
                    <td>{entry.year}</td>
                  </tr>
                ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default Leaderboard;
