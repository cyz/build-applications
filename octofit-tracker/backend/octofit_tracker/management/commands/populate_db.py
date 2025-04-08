from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        self.stdout.write(self.style.NOTICE('Creating sample data for Octofit Tracker...'))

        # Create users
        users = [
            User(_id=ObjectId(), username='aquaracer', email='aquaracer@mergington.edu', password='password123'),
            User(_id=ObjectId(), username='deepsea', email='deepsea@mergington.edu', password='password123'),
            User(_id=ObjectId(), username='coralguardian', email='coralguardian@mergington.edu', password='password123'),
            User(_id=ObjectId(), username='tidechaser', email='tidechaser@mergington.edu', password='password123'),
            User(_id=ObjectId(), username='wavesurfer', email='wavesurfer@mergington.edu', password='password123'),
        ]
        User.objects.bulk_create(users)
        self.stdout.write(self.style.SUCCESS('Created 5 sample users'))

        # Create teams
        teams = [
            Team(_id=ObjectId(), name='Octopus Squad', description='The underwater masters'),
            Team(_id=ObjectId(), name='Reef Rangers', description='Protectors of the reef'),
        ]
        
        # Save teams first
        for team in teams:
            team.save()
        
        # Now add members
        teams[0].members.add(users[0], users[1], users[2])
        teams[1].members.add(users[3], users[4])
        
        for team in teams:
            team.save()
            
        self.stdout.write(self.style.SUCCESS(f'Created {len(teams)} teams with members'))

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='swimming', duration=timedelta(hours=1), distance=2.5, calories=400, notes='Morning swim'),
            Activity(_id=ObjectId(), user=users[1], activity_type='cycling', duration=timedelta(hours=2), distance=30, calories=800, notes='Afternoon ride'),
            Activity(_id=ObjectId(), user=users[2], activity_type='running', duration=timedelta(minutes=45), distance=5, calories=350, notes='Evening jog'),
            Activity(_id=ObjectId(), user=users[3], activity_type='strength', duration=timedelta(minutes=50), calories=300, notes='Weight training'),
            Activity(_id=ObjectId(), user=users[4], activity_type='crossfit', duration=timedelta(hours=1), calories=500, notes='Intense session'),
        ]
        Activity.objects.bulk_create(activities)
        self.stdout.write(self.style.SUCCESS('Created sample activities'))

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], score=95, week=14, year=2025),
            Leaderboard(_id=ObjectId(), user=users[1], score=88, week=14, year=2025),
            Leaderboard(_id=ObjectId(), user=users[2], score=92, week=14, year=2025),
            Leaderboard(_id=ObjectId(), user=users[3], score=78, week=14, year=2025),
            Leaderboard(_id=ObjectId(), user=users[4], score=85, week=14, year=2025),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)
        self.stdout.write(self.style.SUCCESS('Created sample leaderboard entries'))

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Ocean Swimming', description='Long distance swim training', difficulty=2, activity_type='swimming', duration=timedelta(minutes=45)),
            Workout(_id=ObjectId(), name='Beach Run', description='Running along the shoreline', difficulty=1, activity_type='running', duration=timedelta(minutes=30)),
            Workout(_id=ObjectId(), name='Full Body Challenge', description='Comprehensive strength workout', difficulty=3, activity_type='strength', duration=timedelta(minutes=60)),
            Workout(_id=ObjectId(), name='Cycling Tour', description='Scenic cycling route', difficulty=2, activity_type='cycling', duration=timedelta(hours=1, minutes=30)),
            Workout(_id=ObjectId(), name='Water Aerobics', description='Low-impact water exercises', difficulty=1, activity_type='swimming', duration=timedelta(minutes=45)),
        ]
        Workout.objects.bulk_create(workouts)
        self.stdout.write(self.style.SUCCESS('Created sample workouts'))

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data for Octofit Tracker!'))
