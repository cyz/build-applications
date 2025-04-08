#!/usr/bin/env python3
# filepath: /workspaces/build-applications/octofit-tracker/backend/populate_octofit_db.py

"""
Script para popular o banco de dados octofit_db com dados de teste
para o aplicativo OctoFit das escolas de Merington.
"""

from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime, timedelta
import sys

def main():
    print("Iniciando a população do banco de dados octofit_db...")
    
    # Conectar ao MongoDB
    try:
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        print("Conectado ao MongoDB com sucesso!")
    except Exception as e:
        print(f"Erro ao conectar ao MongoDB: {e}")
        sys.exit(1)
    
    # Limpar coleções existentes
    try:
        db.users.drop()
        db.teams.drop()
        db.activities.drop()
        db.leaderboard.drop()
        db.workouts.drop()
        print("Coleções anteriores removidas com sucesso!")
    except Exception as e:
        print(f"Erro ao limpar coleções existentes: {e}")
        sys.exit(1)
    
    # Criar usuários
    users = [
        {
            "_id": ObjectId(),
            "username": "aquaracer",
            "email": "aquaracer@mergington.edu",
            "password": "password123",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "_id": ObjectId(),
            "username": "deepsea",
            "email": "deepsea@mergington.edu",
            "password": "password123",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "_id": ObjectId(),
            "username": "coralguardian",
            "email": "coralguardian@mergington.edu",
            "password": "password123",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "_id": ObjectId(),
            "username": "tidechaser",
            "email": "tidechaser@mergington.edu",
            "password": "password123",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "_id": ObjectId(),
            "username": "wavesurfer",
            "email": "wavesurfer@mergington.edu",
            "password": "password123",
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
    ]
    
    try:
        user_ids = db.users.insert_many(users).inserted_ids
        print(f"Criados {len(user_ids)} usuários com sucesso!")
    except Exception as e:
        print(f"Erro ao criar usuários: {e}")
        sys.exit(1)
    
    # Criar equipes
    teams = [
        {
            "_id": ObjectId(),
            "name": "Octopus Squad",
            "description": "The underwater masters",
            "created_at": datetime.now(),
            "members": [user_ids[0], user_ids[1], user_ids[2]]
        },
        {
            "_id": ObjectId(),
            "name": "Reef Rangers",
            "description": "Protectors of the reef",
            "created_at": datetime.now(),
            "members": [user_ids[3], user_ids[4]]
        }
    ]
    
    try:
        team_ids = db.teams.insert_many(teams).inserted_ids
        print(f"Criadas {len(team_ids)} equipes com sucesso!")
    except Exception as e:
        print(f"Erro ao criar equipes: {e}")
        sys.exit(1)
    
    # Criar atividades (utilizando funções auxiliares para tratar os tipos de dados complexos)
    def duration_to_seconds(hours=0, minutes=0):
        return hours * 3600 + minutes * 60
    
    activities = [
        {
            "_id": ObjectId(),
            "user": user_ids[0],
            "activity_type": "swimming",
            "duration": duration_to_seconds(hours=1),
            "distance": 2.5,
            "calories": 400,
            "notes": "Morning swim",
            "created_at": datetime.now()
        },
        {
            "_id": ObjectId(),
            "user": user_ids[1],
            "activity_type": "cycling",
            "duration": duration_to_seconds(hours=2),
            "distance": 30,
            "calories": 800,
            "notes": "Afternoon ride",
            "created_at": datetime.now()
        },
        {
            "_id": ObjectId(),
            "user": user_ids[2],
            "activity_type": "running",
            "duration": duration_to_seconds(minutes=45),
            "distance": 5,
            "calories": 350,
            "notes": "Evening jog",
            "created_at": datetime.now()
        },
        {
            "_id": ObjectId(),
            "user": user_ids[3],
            "activity_type": "strength",
            "duration": duration_to_seconds(minutes=50),
            "calories": 300,
            "notes": "Weight training",
            "created_at": datetime.now()
        },
        {
            "_id": ObjectId(),
            "user": user_ids[4],
            "activity_type": "crossfit",
            "duration": duration_to_seconds(hours=1),
            "calories": 500,
            "notes": "Intense session",
            "created_at": datetime.now()
        }
    ]
    
    try:
        activity_ids = db.activities.insert_many(activities).inserted_ids
        print(f"Criadas {len(activity_ids)} atividades com sucesso!")
    except Exception as e:
        print(f"Erro ao criar atividades: {e}")
        sys.exit(1)
    
    # Criar entradas de leaderboard
    leaderboard_entries = [
        {
            "_id": ObjectId(),
            "user": user_ids[0],
            "score": 95,
            "week": 14,
            "year": 2025,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "_id": ObjectId(),
            "user": user_ids[1],
            "score": 88,
            "week": 14,
            "year": 2025,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "_id": ObjectId(),
            "user": user_ids[2],
            "score": 92,
            "week": 14,
            "year": 2025,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "_id": ObjectId(),
            "user": user_ids[3],
            "score": 78,
            "week": 14,
            "year": 2025,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "_id": ObjectId(),
            "user": user_ids[4],
            "score": 85,
            "week": 14,
            "year": 2025,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
    ]
    
    try:
        leaderboard_ids = db.leaderboard.insert_many(leaderboard_entries).inserted_ids
        print(f"Criadas {len(leaderboard_ids)} entradas de leaderboard com sucesso!")
    except Exception as e:
        print(f"Erro ao criar entradas de leaderboard: {e}")
        sys.exit(1)
    
    # Criar treinos
    workouts = [
        {
            "_id": ObjectId(),
            "name": "Ocean Swimming",
            "description": "Long distance swim training",
            "difficulty": 2,
            "activity_type": "swimming",
            "duration": duration_to_seconds(minutes=45),
            "created_at": datetime.now()
        },
        {
            "_id": ObjectId(),
            "name": "Beach Run",
            "description": "Running along the shoreline",
            "difficulty": 1,
            "activity_type": "running",
            "duration": duration_to_seconds(minutes=30),
            "created_at": datetime.now()
        },
        {
            "_id": ObjectId(),
            "name": "Full Body Challenge",
            "description": "Comprehensive strength workout",
            "difficulty": 3,
            "activity_type": "strength",
            "duration": duration_to_seconds(minutes=60),
            "created_at": datetime.now()
        },
        {
            "_id": ObjectId(),
            "name": "Cycling Tour",
            "description": "Scenic cycling route",
            "difficulty": 2,
            "activity_type": "cycling",
            "duration": duration_to_seconds(hours=1, minutes=30),
            "created_at": datetime.now()
        },
        {
            "_id": ObjectId(),
            "name": "Water Aerobics",
            "description": "Low-impact water exercises",
            "difficulty": 1,
            "activity_type": "swimming",
            "duration": duration_to_seconds(minutes=45),
            "created_at": datetime.now()
        }
    ]
    
    try:
        workout_ids = db.workouts.insert_many(workouts).inserted_ids
        print(f"Criados {len(workout_ids)} treinos com sucesso!")
    except Exception as e:
        print(f"Erro ao criar treinos: {e}")
        sys.exit(1)
    
    # Adicionar índices para garantir IDs únicos e melhorar a performance
    try:
        db.users.create_index("email", unique=True)
        db.teams.create_index("name", unique=True)
        print("Índices criados com sucesso!")
    except Exception as e:
        print(f"Erro ao criar índices: {e}")
        sys.exit(1)
    
    print("\nBanco de dados octofit_db populado com sucesso para o aplicativo OctoFit da escola de Merington!")
    print("Resumo:")
    print(f"- {len(user_ids)} usuários criados")
    print(f"- {len(team_ids)} equipes criadas")
    print(f"- {len(activity_ids)} atividades criadas")
    print(f"- {len(leaderboard_ids)} entradas de leaderboard criadas")
    print(f"- {len(workout_ids)} treinos criados")

if __name__ == "__main__":
    main()
