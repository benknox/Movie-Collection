from django.contrib.auth.models import User, Group
from .models import Movie
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class MovieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Movie
		fields = ['id', 'name', 'duration']
		read_only_fields = ['id']