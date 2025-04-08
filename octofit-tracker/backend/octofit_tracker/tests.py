# filepath: /workspaces/build-applications/octofit-tracker/backend/octofit_tracker/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta
from bson.objectid import ObjectId


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_user_creation(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertEqual(self.user.__str__(), 'testuser')
        self.assertEqual(User.objects.count(), 1)


class TeamModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.team = Team.objects.create(
            name='Test Team',
            description='This is a test team'
        )
        self.team.members.add(self.user)

    def test_team_creation(self):
        self.assertTrue(isinstance(self.team, Team))
        self.assertEqual(self.team.__str__(), 'Test Team')
        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(self.team.members.count(), 1)


class ActivityModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.activity = Activity.objects.create(
            user=self.user,
            activity_type='running',
            duration=timedelta(minutes=30),
            distance=5.0,
            calories=300,
            notes='Morning run'
        )

    def test_activity_creation(self):
        self.assertTrue(isinstance(self.activity, Activity))
        self.assertEqual(Activity.objects.count(), 1)
        self.assertEqual(self.activity.user, self.user)
        self.assertEqual(self.activity.activity_type, 'running')


class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.leaderboard_entry = Leaderboard.objects.create(
            user=self.user,
            score=100,
            week=1,
            year=2025
        )

    def test_leaderboard_creation(self):
        self.assertTrue(isinstance(self.leaderboard_entry, Leaderboard))
        self.assertEqual(Leaderboard.objects.count(), 1)
        self.assertEqual(self.leaderboard_entry.user, self.user)
        self.assertEqual(self.leaderboard_entry.score, 100)


class WorkoutModelTest(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Test Workout',
            description='This is a test workout',
            difficulty=2,
            activity_type='running',
            duration=timedelta(minutes=45)
        )

    def test_workout_creation(self):
        self.assertTrue(isinstance(self.workout, Workout))
        self.assertEqual(Workout.objects.count(), 1)
        self.assertEqual(self.workout.name, 'Test Workout')
        self.assertEqual(self.workout.difficulty, 2)


class APITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.team = Team.objects.create(
            name='Test Team',
            description='This is a test team'
        )
        self.team.members.add(self.user)
        self.activity = Activity.objects.create(
            user=self.user,
            activity_type='running',
            duration=timedelta(minutes=30),
            distance=5.0,
            calories=300,
            notes='Morning run'
        )
        self.leaderboard_entry = Leaderboard.objects.create(
            user=self.user,
            score=100,
            week=1,
            year=2025
        )
        self.workout = Workout.objects.create(
            name='Test Workout',
            description='This is a test workout',
            difficulty=2,
            activity_type='running',
            duration=timedelta(minutes=45)
        )

    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)

    def test_get_users(self):
        response = self.client.get(reverse('user-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_teams(self):
        response = self.client.get(reverse('team-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_activities(self):
        response = self.client.get(reverse('activity-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_leaderboard(self):
        response = self.client.get(reverse('leaderboard-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_workouts(self):
        response = self.client.get(reverse('workout-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
