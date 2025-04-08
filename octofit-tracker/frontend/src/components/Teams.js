import React, { useEffect, useState } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTeams = async () => {
      try {
        const response = await fetch('https://organic-halibut-w9x4v57r4hgrgg-8000.app.github.dev/api/teams/');
        if (!response.ok) {
          throw new Error(`Erro HTTP: ${response.status}`);
        }
        const data = await response.json();
        setTeams(data.results || data);
        setLoading(false);
      } catch (error) {
        setError(`Falha ao carregar equipes: ${error.message}`);
        setLoading(false);
      }
    };

    fetchTeams();
  }, []);

  if (loading) return <div className="text-center mt-5"><div className="spinner-border text-primary" role="status"><span className="visually-hidden">Carregando...</span></div></div>;
  if (error) return <div className="alert alert-danger mt-3">{error}</div>;

  return (
    <div className="teams-container">
      <h1 className="mb-4 text-center">Equipes</h1>
      {teams.length === 0 ? (
        <p className="text-center">Nenhuma equipe encontrada.</p>
      ) : (
        <div className="row">
          {teams.map((team) => (
            <div key={team._id} className="col-md-6 col-lg-4 mb-4">
              <div className="card h-100">
                <div className="card-header bg-primary text-white">
                  <h5 className="card-title mb-0">{team.name}</h5>
                </div>
                <div className="card-body">
                  <p className="card-text">{team.description || 'Sem descrição'}</p>
                  <h6>Membros ({team.members?.length || 0}):</h6>
                  {team.members && team.members.length > 0 ? (
                    <ul className="list-group">
                      {team.members.map((member) => (
                        <li key={member._id} className="list-group-item">
                          {member.username || 'Nome não disponível'}
                        </li>
                      ))}
                    </ul>
                  ) : (
                    <p>Nenhum membro nesta equipe.</p>
                  )}
                </div>
                <div className="card-footer text-muted">
                  Criado em: {new Date(team.created_at).toLocaleDateString()}
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default Teams;
