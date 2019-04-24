from rest_framework import serializers
from .models import Map, Spot, Edge, Shuttle, Route, Building, Restaurant, Seminar, Lecture, Post

class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = ('id', 'latitude', 'longitude')

class MapSerializer(serializers.ModelSerializer):
    spots = SpotSerializer(many=True, read_only=True)
    class Meta:
        model = Map
        fields = ('id', 'link', 'spots')

class EdgeSerializer(serializers.ModelSerializer):
    spots = SpotSerializer(many=True, read_only=True)
    class Meta:
        model = Edge
        fields = ('id', 'spots')

class ShuttleSerializer(serializers.ModelSerializer):
    edges = EdgeSerializer(many=True, read_only=True)
    class Meta:
        model = Shuttle
        fields = ('id','kr_name', 'en_name', 'operating_hours', 'info', 'edges')

class RouteSerializer(serializers.ModelSerializer):
    start = SpotSerializer(read_only=True)
    end = SpotSerializer(read_only=True)
    edges = EdgeSerializer(many=True, read_only=True)
    class Meta:
        model = Route
        fields = ('start', 'end', 'length', 'edges')

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class SeminarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seminar
        fields = '__all__'

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class BuildingSerializer(serializers.ModelSerializer):
    spot = SpotSerializer(read_only=True)
    restaurants = RestaurantSerializer(many=True, read_only=True)
    seminars = SeminarSerializer(many=True, read_only=True)
    lectures = LectureSerializer(many=True, read_only=True)
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Building
        fields = ('id', 'code','kr_name', 'en_name', 'spot', 'latitude', 'longitude', 'info', 'restaurants','seminars','lectures','posts')