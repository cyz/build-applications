// filepath: /workspaces/build-applications/octofit-tracker/backend/populate_octofit_db.js
// Script para popular o banco de dados octofit_db com dados de teste para o OctoFit

// Conectar ao banco de dados octofit_db
db = db.getSiblingDB('octofit_db');

// Limpar coleções existentes
db.users.drop();
db.teams.drop();
db.activities.drop();
db.leaderboard.drop();
db.workouts.drop();

print("Coleções anteriores removidas com sucesso!");

// Criar usuários
var user1 = db.users.insertOne({
    username: "aquaracer",
    email: "aquaracer@mergington.edu",
    password: "password123",
    created_at: new Date(),
    updated_at: new Date()
});

var user2 = db.users.insertOne({
    username: "deepsea",
    email: "deepsea@mergington.edu",
    password: "password123",
    created_at: new Date(),
    updated_at: new Date()
});

var user3 = db.users.insertOne({
    username: "coralguardian",
    email: "coralguardian@mergington.edu",
    password: "password123",
    created_at: new Date(),
    updated_at: new Date()
});

var user4 = db.users.insertOne({
    username: "tidechaser",
    email: "tidechaser@mergington.edu",
    password: "password123",
    created_at: new Date(),
    updated_at: new Date()
});

var user5 = db.users.insertOne({
    username: "wavesurfer",
    email: "wavesurfer@mergington.edu",
    password: "password123",
    created_at: new Date(),
    updated_at: new Date()
});

print("Usuários criados com sucesso!");

// Criar equipes
var team1 = db.teams.insertOne({
    name: "Octopus Squad",
    description: "The underwater masters",
    created_at: new Date(),
    members: [user1.insertedId, user2.insertedId, user3.insertedId]
});

var team2 = db.teams.insertOne({
    name: "Reef Rangers",
    description: "Protectors of the reef",
    created_at: new Date(),
    members: [user4.insertedId, user5.insertedId]
});

print("Equipes criadas com sucesso!");

// Criar atividades
db.activities.insertMany([
    {
        user: user1.insertedId,
        activity_type: "swimming",
        duration: 3600, // 1 hora em segundos
        distance: 2.5,
        calories: 400,
        notes: "Morning swim",
        created_at: new Date()
    },
    {
        user: user2.insertedId,
        activity_type: "cycling",
        duration: 7200, // 2 horas em segundos
        distance: 30,
        calories: 800,
        notes: "Afternoon ride",
        created_at: new Date()
    },
    {
        user: user3.insertedId,
        activity_type: "running",
        duration: 2700, // 45 minutos em segundos
        distance: 5,
        calories: 350,
        notes: "Evening jog",
        created_at: new Date()
    },
    {
        user: user4.insertedId,
        activity_type: "strength",
        duration: 3000, // 50 minutos em segundos
        calories: 300,
        notes: "Weight training",
        created_at: new Date()
    },
    {
        user: user5.insertedId,
        activity_type: "crossfit",
        duration: 3600, // 1 hora em segundos
        calories: 500,
        notes: "Intense session",
        created_at: new Date()
    }
]);

print("Atividades criadas com sucesso!");

// Criar entradas de leaderboard
db.leaderboard.insertMany([
    {
        user: user1.insertedId,
        score: 95,
        week: 14,
        year: 2025,
        created_at: new Date(),
        updated_at: new Date()
    },
    {
        user: user2.insertedId,
        score: 88,
        week: 14,
        year: 2025,
        created_at: new Date(),
        updated_at: new Date()
    },
    {
        user: user3.insertedId,
        score: 92,
        week: 14,
        year: 2025,
        created_at: new Date(),
        updated_at: new Date()
    },
    {
        user: user4.insertedId,
        score: 78,
        week: 14,
        year: 2025,
        created_at: new Date(),
        updated_at: new Date()
    },
    {
        user: user5.insertedId,
        score: 85,
        week: 14,
        year: 2025,
        created_at: new Date(),
        updated_at: new Date()
    }
]);

print("Entradas de leaderboard criadas com sucesso!");

// Criar treinos
db.workouts.insertMany([
    {
        name: "Ocean Swimming",
        description: "Long distance swim training",
        difficulty: 2,
        activity_type: "swimming",
        duration: 2700, // 45 minutos em segundos
        created_at: new Date()
    },
    {
        name: "Beach Run",
        description: "Running along the shoreline",
        difficulty: 1,
        activity_type: "running",
        duration: 1800, // 30 minutos em segundos
        created_at: new Date()
    },
    {
        name: "Full Body Challenge",
        description: "Comprehensive strength workout",
        difficulty: 3,
        activity_type: "strength",
        duration: 3600, // 60 minutos em segundos
        created_at: new Date()
    },
    {
        name: "Cycling Tour",
        description: "Scenic cycling route",
        difficulty: 2,
        activity_type: "cycling",
        duration: 5400, // 1 hora e 30 minutos em segundos
        created_at: new Date()
    },
    {
        name: "Water Aerobics",
        description: "Low-impact water exercises",
        difficulty: 1,
        activity_type: "swimming",
        duration: 2700, // 45 minutos em segundos
        created_at: new Date()
    }
]);

print("Treinos criados com sucesso!");

// Criar índices para melhorar a performance e garantir unicidade
db.users.createIndex({ "email": 1 }, { unique: true });
db.teams.createIndex({ "name": 1 }, { unique: true });

print("Índices criados com sucesso!");

print("\nBanco de dados octofit_db populado com sucesso para o aplicativo OctoFit da escola de Merington!");
