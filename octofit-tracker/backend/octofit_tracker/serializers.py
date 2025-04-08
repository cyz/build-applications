from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)

class UserSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

class TeamSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    members = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = '__all__'
    
    def get_members(self, obj):
        return UserSerializer(obj.members.all(), many=True).data

class ActivitySerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    user_details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Activity
        fields = ['_id', 'user', 'user_details', 'activity_type', 'duration', 
                  'distance', 'calories', 'notes', 'created_at']
    
    def get_user_details(self, obj):
        return UserSerializer(obj.user).data

class LeaderboardSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)
    user_details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Leaderboard
        fields = ['_id', 'user', 'user_details', 'score', 'week', 'year', 'created_at', 'updated_at']
    
    def get_user_details(self, obj):
        return UserSerializer(obj.user).data

class WorkoutSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)

    class Meta:
        model = Workout
        fields = '__all__'
