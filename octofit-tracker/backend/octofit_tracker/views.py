from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from .models import User, Team, Activity, Leaderboard, Workout

@api_view(['GET'])
def api_root(request, format=None):
    """
    The root endpoint for the OctoFit Tracker API.
    """
    base_url = 'https://organic-halibut-w9x4v57r4hgrgg-8000.app.github.dev/'
    return Response({
        'users': base_url + 'api/users/',
        'teams': base_url + 'api/teams/',
        'activities': base_url + 'api/activities/',
        'leaderboard': base_url + 'api/leaderboard/',
        'workouts': base_url + 'api/workouts/',
    })

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows activities to be viewed or edited.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def get_queryset(self):
        """
        Optionally filter activities by user ID.
        """
        queryset = Activity.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(user=user_id)
        return queryset


class LeaderboardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows leaderboard entries to be viewed or edited.
    """
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

    def get_queryset(self):
        """
        Optionally filter leaderboard by week and year.
        """
        queryset = Leaderboard.objects.all()
        week = self.request.query_params.get('week', None)
        year = self.request.query_params.get('year', None)
        
        if week is not None and year is not None:
            queryset = queryset.filter(week=week, year=year)
        return queryset


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows workouts to be viewed or edited.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    
    def get_queryset(self):
        """
        Optionally filter workouts by activity type or difficulty.
        """
        queryset = Workout.objects.all()
        activity_type = self.request.query_params.get('activity_type', None)
        difficulty = self.request.query_params.get('difficulty', None)
        
        if activity_type is not None:
            queryset = queryset.filter(activity_type=activity_type)
        if difficulty is not None:
            queryset = queryset.filter(difficulty=difficulty)
        return queryset
