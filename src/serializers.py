from django.contrib.auth.models import User, Group
from .models import Movie
from rest_framework import serializers

#TODO: try upgrading everything to a HyperlinkedModelSerializer
class UserSerializer(serializers.ModelSerializer):
	movies = serializers.PrimaryKeyRelatedField(many=True, queryset=Movie.objects.all())
	class Meta:
		model = User
		#fields = ['url', 'username', 'email', 'groups']
		fields = ['id', 'username', 'email', 'groups', 'movies']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ['url', 'name']

class MovieSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	ownerId = serializers.ReadOnlyField(source='owner.id')
	class Meta:
		model = Movie
		fields = ['id', 'name', 'duration', 'owner', 'ownerId']
		read_only_fields = ['id']