from rest_framework import serializers
from .models import Map, Spot, Edge, Shuttle, Route, Building, Restaurant, Seminar, Lecture, Post, Cafe, Conv, Bank, Atm, Comment

class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = ('id', 'latitude', 'longitude')

class BuildingBasicSerializer(serializers.ModelSerializer):
    spot = SpotSerializer(read_only=True)
    class Meta:
        model = Building
        fields = ('id', 'code','kr_name', 'en_name', 'spot')

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
    building = BuildingBasicSerializer(read_only=True)
    class Meta:
        model = Restaurant
        fields = '__all__'

class CafeSerializer(serializers.ModelSerializer):
    building = BuildingBasicSerializer(read_only=True)
    class Meta:
        model = Cafe
        fields = '__all__'

class ConvSerializer(serializers.ModelSerializer):
    building = BuildingBasicSerializer(read_only=True)
    class Meta:
        model = Conv
        fields = '__all__'

class BankSerializer(serializers.ModelSerializer):
    building = BuildingBasicSerializer(read_only=True)
    class Meta:
        model = Bank
        fields = '__all__'

class AtmSerializer(serializers.ModelSerializer):
    building = BuildingBasicSerializer(read_only=True)
    class Meta:
        model = Atm
        fields = '__all__'

class SeminarSerializer(serializers.ModelSerializer):
    building = BuildingBasicSerializer(read_only=True)
    class Meta:
        model = Seminar
        fields = '__all__'

class LectureSerializer(serializers.ModelSerializer):
    building = BuildingBasicSerializer(read_only=True)
    class Meta:
        model = Lecture
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','created', 'content', 'username', 'post', 'like')

class PostSerializer(serializers.ModelSerializer):
    building = BuildingBasicSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('id','created','title', 'content', 'username', 'building', 'like', 'comments')

class BuildingSerializer(serializers.ModelSerializer):
    spot = SpotSerializer(read_only=True)
    restaurants = RestaurantSerializer(many=True, read_only=True)
    cafes = CafeSerializer(many=True, read_only=True)
    convs = ConvSerializer(many=True, read_only=True)
    banks = BankSerializer(many=True, read_only=True)
    atms = AtmSerializer(many=True, read_only=True)
    seminars = SeminarSerializer(many=True, read_only=True)
    lectures = LectureSerializer(many=True, read_only=True)
    posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = Building
        fields = ('id', 'code','kr_name', 'en_name', 'spot', 'latitude', 'longitude', 'info', 'restaurants','cafes','convs','banks','atms','seminars','lectures','posts')