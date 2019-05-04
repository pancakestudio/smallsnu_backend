from django.test import TestCase
from .models import Map, Spot, Edge, Shuttle, Route, Building, Restaurant, Seminar, Lecture, Post
import json
# Create your tests here.

class RestTests(TestCase):
    def setUp(self):
        #Load buildings.json
        with open('buildings.json') as data_file_building:
            building_data = json.load(data_file_building)

        #Load restaurants.json
        with open('restaurants.json') as data_file_restaurant:
            restaurant_data = json.load(data_file_restaurant)

        #Map
        Map(
            link="https://www.openstreetmap.org/node/357964484#map=18/37.45911/126.95242&layers=N",
        ).save()

        #Spot & Building
        for building in building_data:
            latitude_mean = (building['coord_1'][0]+building['coord_2'][0]+building['coord_3'][0]+building['coord_4'][0])/(4.0)
            longitude_mean = (building['coord_1'][1]+building['coord_2'][1]+building['coord_3'][1]+building['coord_4'][1])/(4.0)
            spot = Spot(
                latitude=latitude_mean,
                longitude=longitude_mean,
                map=Map.objects.all()[0]
            )
            spot.save()
            Building(
                code = building["building_no"],
                kr_name = building["building_no"] + " 동",
                en_name = building["building_no"] + " building",
                spot = spot,
                latitude = spot.latitude,
                longitude = spot.longitude,
                info = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. A cras semper auctor neque vitae tempus quam pellentesque. Nibh ipsum consequat nisl vel pretium lectus quam id. Lectus sit amet est placerat in egestas. Mi sit amet mauris commodo quis imperdiet massa. Arcu non odio euismod lacinia at quis risus sed. Eget nunc scelerisque viverra mauris in aliquam sem fringilla. Egestas sed sed risus pretium quam. Blandit libero volutpat sed cras. Rutrum quisque non tellus orci ac auctor augue. Mauris in aliquam sem fringilla. Porttitor lacus luctus accumsan tortor posuere ac ut consequat. Porttitor massa id neque aliquam vestibulum morbi blandit cursus risus. Neque laoreet suspendisse interdum consectetur libero. Morbi tristique senectus et netus et malesuada fames ac. Diam quis enim lobortis scelerisque fermentum dui faucibus in ornare. Volutpat lacus laoreet non curabitur gravida arcu ac tortor dignissim. Quis eleifend quam adipiscing vitae proin sagittis. Nibh ipsum consequat nisl vel. Id leo in vitae turpis massa sed."
            ).save()

        #Restaurant
        for restaurant in restaurant_data:
            Restaurant(
                code=restaurant["code"],
                kr_name=restaurant["kr_name"],
                en_name=restaurant["en_name"],
                building=Building.objects.get(code=restaurant["building_no"]),
                operating_hours=restaurant["operating_hours"]
            ).save()

        #Seminar

        #Lecture

        #Post
        for building in Building.objects.all():
            for content_num in range(1,6):
                Post(
                    title = "testing post " + str(content_num),
                    content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Dui id ornare arcu odio ut sem nulla pharetra diam. Enim diam vulputate ut pharetra sit amet aliquam. Nullam vehicula ipsum a arcu cursus. Egestas diam in arcu cursus. Mauris pellentesque pulvinar ",
                    username = "test user",
                    password = "1234",
                    building = building
                ).save()
    def test_map_list(self):
        response = self.client.get('/map/')
        data = response.json()
        self.assertEqual(response.status_code, 200)

    def test_building_list(self):
        response = self.client.get('/building/')
        data = response.json()
        self.assertEqual(response.status_code, 200)

    def test_building_detail(self):
        response = self.client.get('/building/1/')
        data = response.json()
        self.assertEqual(response.status_code, 200)

    def test_building_post_service(self):
        response = self.client.post('/building/1/post/', json.dumps({'title': 'testing', 'content': '', 'username': 't1', 'password': '1234'}), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/building/1/post/', json.dumps({'title': 'testing', 'content': 'not empty', 'username': 't1', 'password': '1234'}), content_type="application/json")
        self.assertEqual(response.status_code, 201)
        data = response.json()
        postId = data['id']
        response = self.client.post('/post/'+str(postId)+'/', json.dumps({'title': 'testing2', 'content': 'not empty not empty', 'username': 't1 t1', 'password': '1233'}), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        response = self.client.post('/post/'+str(postId)+'/', json.dumps({'title': 'testing2', 'content': 'not empty not empty', 'username': 't1 t1', 'password': '1234'}), content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_seminar_list(self):
        response = self.client.get('/seminar/')
        data = response.json()
        self.assertEqual(response.status_code, 200)

    def test_restaurant_list(self):
        response = self.client.get('/restaurant/')
        data = response.json()
        self.assertEqual(response.status_code, 200)

    def test_shuttle_list(self):
        response = self.client.get('/shuttle/')
        data = response.json()
        self.assertEqual(response.status_code, 200)

    def test_lecture_list(self):
        response = self.client.get('/lecture/')
        data = response.json()
        self.assertEqual(response.status_code, 200)

    def test_route_list(self):
        response = self.client.get('/route/', {'from': 'here', 'to': 'there'})
        data = response.json()
        self.assertEqual(response.status_code, 200)