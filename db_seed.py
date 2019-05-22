import json

from snumap.models import Map, Spot, Edge, Shuttle, Route, Building, Restaurant, Seminar, Lecture, Post

#Load buildings.json
with open('buildings3.json') as data_file_building:
    building_data = json.load(data_file_building)

#Load restaurants.json
with open('restaurants.json') as data_file_restaurant:    
    restaurant_data = json.load(data_file_restaurant)

#Map
Map(
    link="https://www.openstreetmap.org/node/357964484#map=18/37.45911/126.95242&layers=N",
).save()

#Spot
# for building in building_data:
#     latitude_mean = (building['coord_1'][0]+building['coord_2'][0]+building['coord_3'][0]+building['coord_4'][0])/(4.0)
#     longitude_mean = (building['coord_1'][1]+building['coord_2'][1]+building['coord_3'][1]+building['coord_4'][1])/(4.0)
#     Spot(
#         latitude=latitude_mean,
#         longitude=longitude_mean,
#         map=Map.objects.all()[0]
#     ).save()

#Edge

#Shuttle

#Route





#Building
# for index, building in enumerate(building_data):
#     try:
#         spot_located = Spot.objects.get(id=(index+1))
#     except Spot.DoesNotExist:
#         print("error: no such a building spot!")
#     except Spot.MultipleObjectsReturned:
#         print("error: there is duplicated building spots!")
#     Building(
#         code = building["building_no"],
#         kr_name = building["building_no"] + " 동",
#         en_name = building["building_no"] + " building",
#         spot = spot_located,
#         latitude = spot_located.latitude,
#         longitude = spot_located.longitude,
#         info = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. A cras semper auctor neque vitae tempus quam pellentesque. Nibh ipsum consequat nisl vel pretium lectus quam id. Lectus sit amet est placerat in egestas. Mi sit amet mauris commodo quis imperdiet massa. Arcu non odio euismod lacinia at quis risus sed. Eget nunc scelerisque viverra mauris in aliquam sem fringilla. Egestas sed sed risus pretium quam. Blandit libero volutpat sed cras. Rutrum quisque non tellus orci ac auctor augue. Mauris in aliquam sem fringilla. Porttitor lacus luctus accumsan tortor posuere ac ut consequat. Porttitor massa id neque aliquam vestibulum morbi blandit cursus risus. Neque laoreet suspendisse interdum consectetur libero. Morbi tristique senectus et netus et malesuada fames ac. Diam quis enim lobortis scelerisque fermentum dui faucibus in ornare. Volutpat lacus laoreet non curabitur gravida arcu ac tortor dignissim. Quis eleifend quam adipiscing vitae proin sagittis. Nibh ipsum consequat nisl vel. Id leo in vitae turpis massa sed."
#     ).save()


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
        kr_name = building["kr_name"],
        en_name = building["en_name"],
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