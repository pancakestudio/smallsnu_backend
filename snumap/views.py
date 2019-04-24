from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Map, Spot, Edge, Shuttle, Route, Building, Restaurant, Seminar, Lecture, Post
from .serializers import SpotSerializer, MapSerializer, EdgeSerializer, ShuttleSerializer, RouteSerializer, RestaurantSerializer, SeminarSerializer, LectureSerializer, PostSerializer, BuildingSerializer
import json

@api_view(['GET'])
def map_list(request):
    maps = Map.objects.all()
    serializer = MapSerializer(maps, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def building_list(request):
    buildings = Building.objects.all()
    serializer = BuildingSerializer(buildings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def building_detail(request, pk):
    building = Building.objects.get(pk=pk)
    serializer = BuildingSerializer(building)
    return Response(serializer.data)

@api_view(['POST'])
def building_post(request, pk):
    params = json.loads(request.body.decode("utf-8"))
    building = Building.objects.get(pk=pk)
    post = Post(title=params.get("title", 'no_title'), content=params.get('content', 'no_content'), username=params.get('username', 'no_username'), password=params.get('password', 'no_password'), building=building)
    post.save()
    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def seminar_list(request):
    seminars = Seminar.objects.all()
    serializer = SeminarSerializer(seminars, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def shuttle_list(request):
    shuttles = Shuttle.objects.all()
    serializer = ShuttleSerializer(shuttles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def lecture_list(request):
    lectures = Lecture.objects.all()
    serializer = LectureSerializer(lectures, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def route_list(request):
    start = request.GET.get('from', '')
    end = request.GET.get('to', '')
    routes = Route.objects.all()
    serializer = RouteSerializer(routes, many=True)
    return Response(serializer.data)
