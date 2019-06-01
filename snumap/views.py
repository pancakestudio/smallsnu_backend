from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Map, Spot, Edge, Shuttle, Route, Building, Restaurant, Seminar, Lecture, Post, Cafe, Conv, Bank, Atm, Comment
from .serializers import SpotSerializer, MapSerializer, EdgeSerializer, ShuttleSerializer, RouteSerializer, RestaurantSerializer, SeminarSerializer, LectureSerializer, PostSerializer, BuildingSerializer, CafeSerializer, ConvSerializer, BankSerializer, AtmSerializer, CommentSerializer, BuildingBasicSerializer
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
    building = Building.objects.get(code=pk)
    serializer = BuildingSerializer(building)
    return Response(serializer.data)

@api_view(['GET'])
def building_restaurant(request, pk):
    building = Building.objects.get(code=pk)
    restaurants = Restaurant.objects.filter(building=building)
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def building_cafe(request, pk):
    building = Building.objects.get(code=pk)
    cafes = Cafe.objects.filter(building=building)
    serializer = CafeSerializer(cafes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def building_conv(request, pk):
    building = Building.objects.get(code=pk)
    convs = Conv.objects.filter(building=building)
    serializer = ConvSerializer(convs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def building_bank(request, pk):
    building = Building.objects.get(code=pk)
    banks = Bank.objects.filter(building=building)
    serializer = BankSerializer(banks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def building_atm(request, pk):
    building = Building.objects.get(code=pk)
    atms = Atm.objects.filter(building=building)
    serializer = AtmSerializer(atms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def building_seminar(request, pk):
    building = Building.objects.get(code=pk)
    seminars = Seminar.objects.filter(building=building)
    serializer = SeminarSerializer(seminars, many=True)
    return Response(serializer.data)

# maybe, It need to be modified according to service format...

@api_view(['GET','POST'])
def building_post(request, pk):
    if request.method == 'GET':
        building = Building.objects.get(code=pk)
        posts = Post.objects.filter(building=building)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        params = json.loads(request.body.decode("utf-8"))
        if params.get('content', '') == '':
            content = {'warring': 'empty content is not allowed'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        building = Building.objects.get(code=pk)
        post = Post(title=params.get('title', 'no title'), content=params.get('content', 'empty content'), username=params.get('username', 'someone'), password=params.get('password', ''), building=building)
        post.save()
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','POST','DELETE'])
def building_post_detail(request, postId):
    if request.method == 'GET':
        post = Post.objects.get(pk=postId)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'POST':
        params = json.loads(request.body.decode("utf-8"))
        post = Post.objects.get(pk=postId)
        if post.password == params.get('password', ''):
            post.title = params.get('title', 'no title')
            post.content = params.get('content', 'empty content')
            post.username = params.get('username', 'someone')
            post.save()
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            content = {'warring': 'password is wrong!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        params = json.loads(request.body.decode("utf-8"))
        post = Post.objects.get(pk=postId)
        if post.password == params.get('password', ''):
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            content = {'warring': 'password is wrong!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def building_post_like(request, postId):
    post = Post.objects.get(pk=postId)
    post.like = post.like+1
    post.save()
    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(['GET','POST'])
def building_post_comment(request, postId):
    if request.method == 'GET':
        post = Post.objects.get(pk=postId)
        comments = Comment.objects.filter(post=post)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        params = json.loads(request.body.decode("utf-8"))
        if params.get('content', '') == '':
            content = {'warring': 'empty content is not allowed'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        post = Post.objects.get(pk=postId)
        comment = Comment(content=params.get('content', 'empty content'), username=params.get('username', 'someone'), password=params.get('password', ''), post=post)
        comment.save()
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','POST','DELETE'])
def comment_detail(request, commentId):
    if request.method == 'GET':
        comment = Comment.objects.get(pk=commentId)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'POST':
        params = json.loads(request.body.decode("utf-8"))
        comment = Comment.objects.get(pk=commentId)
        if comment.password == params.get('password', ''):
            comment.content = params.get('content', 'empty content')
            comment.username = params.get('username', 'someone')
            comment.save()
            serializer = CommentSerializer(comment)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            content = {'warring': 'password is wrong!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        params = json.loads(request.body.decode("utf-8"))
        comment = Comment.objects.get(pk=commentId)
        if comment.password == params.get('password', ''):
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            content = {'warring': 'password is wrong!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def comment_like(request, commentId):
    comment = Comment.objects.get(pk=commentId)
    comment.like = comment.like+1
    comment.save()
    serializer = CommentSerializer(comment)
    return Response(serializer.data)

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def seminar_list(request):
    seminars = Seminar.objects.all()
    serializer = SeminarSerializer(seminars, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def seminar_detail(request, pk):
    seminar = Seminar.objects.get(pk=pk)
    serializer = SeminarSerializer(seminar)
    return Response(serializer.data)

@api_view(['GET'])
def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def restaurant_detail(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    serializer = RestaurantSerializer(restaurant)
    return Response(serializer.data)

@api_view(['GET'])
def cafe_list(request):
    cafes = Cafe.objects.all()
    serializer = CafeSerializer(cafes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def cafe_detail(request, pk):
    cafe = Cafe.objects.get(pk=pk)
    serializer = CafeSerializer(cafe)
    return Response(serializer.data)

@api_view(['GET'])
def conv_list(request):
    convs = Conv.objects.all()
    serializer = ConvSerializer(convs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def conv_detail(request, pk):
    conv = Conv.objects.get(pk=pk)
    serializer = ConvSerializer(conv)
    return Response(serializer.data)

@api_view(['GET'])
def bank_list(request):
    banks = Bank.objects.all()
    serializer = BankSerializer(banks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def bank_detail(request, pk):
    bank = Bank.objects.get(pk=pk)
    serializer = BankSerializer(bank)
    return Response(serializer.data)

@api_view(['GET'])
def atm_list(request):
    atms = Atm.objects.all()
    serializer = AtmSerializer(atms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def atm_detail(request, pk):
    atm = Atm.objects.get(pk=pk)
    serializer = AtmSerializer(atm)
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
def lecture_detail(request, pk):
    lecture = Lecture.objects.get(pk=pk)
    serializer = LectureSerializer(lecture)
    return Response(serializer.data)

# have to edit route_list

@api_view(['GET'])
def route_list(request):
    start = request.GET.get('from', '')
    end = request.GET.get('to', '')
    if start == '' or end == '':
        content = {'warring': 'empty start or end is not allowed'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    routes = Route.objects.all()
    serializer = RouteSerializer(routes, many=True)
    return Response(serializer.data)

def contain_keyword_check(origin, keyword):
    origin = origin.lower()
    keyword = keyword.lower()
    currentIndex = -1
    for c in keyword:
        i = origin.find(c)
        if i == -1:
            return False
        if currentIndex < i:
            currentIndex = i
            continue
        else:
            return False
    return True

@api_view(['GET'])
def search(request):
    keyword = request.GET.get('q', '')
    if keyword == '':
        content = {'warring': 'empty keyword is not allowed'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    selected_building_list = Building.objects.filter(info__icontains = keyword)
    selected_id_list = []
    for building in selected_building_list:
        selected_id_list.append(building.id)
    for building in Building.objects.all():
        if contain_keyword_check(building.kr_name, keyword) and (not (building.id in selected_id_list)):
            selected_id_list.append(building.id)
    buildings = Building.objects.filter(id__in=selected_id_list)
    serializer = BuildingBasicSerializer(buildings, many=True)
    return Response(serializer.data)

