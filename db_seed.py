import json
import geopy.distance

from snumap.models import Map, Spot, Edge, Shuttle, Route, Building, Restaurant, Seminar, Lecture, Post, Cafe, Conv, Bank, Atm

#Load buildings3.json
with open('buildings3.json') as data_file_building:
    building_data = json.load(data_file_building)

#Load restaurants_new.json
with open('restaurants_new.json') as data_file_restaurant:    
    restaurant_data = json.load(data_file_restaurant)

#Load cafes.json
with open('cafes.json') as data_file_cafe:
    cafe_data = json.load(data_file_cafe)

#Load convs.json
with open('convs.json') as data_file_conv:    
    conv_data = json.load(data_file_conv)

#Load banks.json
with open('banks.json') as data_file_bank:    
    bank_data = json.load(data_file_bank)

#Load atms.json
with open('atms.json') as data_file_atm:    
    atm_data = json.load(data_file_atm)

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

#Edge
for spot in Spot.objects.all():
    id = spot.id
    targetSpots = Spot.objects.filter(id__gt=id)
    for targetSpot in targetSpots:
        start = (spot.latitude, spot.longitude)
        end = (targetSpot.latitude, targetSpot.longitude)
        length=float(geopy.distance.geodesic(start, end).km)
        if length > 0.2:
            #print("skip: "+ str(spot.id)+"&"+str(targetSpot.id))
            continue
        edge = Edge(
            map=Map.objects.all()[0],
            length=length
        )
        edge.save()
        edge.spots.add(spot)
        edge.spots.add(targetSpot)
        edge.save()
        #print("add: "+ str(spot.id)+"&"+str(targetSpot.id))

#Restaurant
for restaurant in restaurant_data:
    try:
        building=Building.objects.get(code=restaurant["building_no"])
    except:
        print("err rest: "+str(restaurant["building_no"]))
    Restaurant(
        location=restaurant["location"],
        kr_name=restaurant["kr_name"],
        en_name=restaurant["en_name"],
        building=Building.objects.get(code=restaurant["building_no"]),
        operating_hours=restaurant["operating_hours"]
    ).save()

#Cafe
for cafe in cafe_data:
    try:
        building=Building.objects.get(code=cafe["building_no"])
    except:
        print("err cafe: "+str(cafe["building_no"]))
    Cafe(
        location=cafe["location"],
        kr_name=cafe["kr_name"],
        en_name=cafe["en_name"],
        building=Building.objects.get(code=cafe["building_no"]),
        operating_hours=cafe["operating_hours"]
    ).save()

#Conv
for conv in conv_data:
    try:
        building=Building.objects.get(code=conv["building_no"])
    except:
        print("err conv: "+str(conv["building_no"]))
    Conv(
        location=conv["location"],
        kr_name=conv["kr_name"],
        en_name=conv["en_name"],
        building=Building.objects.get(code=conv["building_no"]),
        operating_hours=conv["operating_hours"]
    ).save()

#Bank
for bank in bank_data:
    try:
        building=Building.objects.get(code=bank["building_no"])
    except:
        print("err bank: "+str(bank["building_no"]))
    Bank(
        location=bank["location"],
        kr_name=bank["kr_name"],
        en_name=bank["en_name"],
        building=Building.objects.get(code=bank["building_no"]),
        operating_hours=bank["operating_hours"]
    ).save()

#Atm
for atm in atm_data:
    try:
        building=Building.objects.get(code=atm["building_no"])
    except:
        print("err atm: "+str(atm["building_no"]))
    Atm(
        location=atm["location"],
        kr_name=atm["kr_name"],
        en_name=atm["en_name"],
        building=Building.objects.get(code=atm["building_no"]),
        operating_hours=atm["operating_hours"]
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

#Set building infos
for building in Building.objects.all():
    info = "건물번호:"+building.code+"\n"
    info += "건물이름:"+building.kr_name+"\n"
    info += "건물영어이름:"+building.en_name+"\n"
    #restaurant
    if building.restaurants.count != 0:
        info += "식당:"
    for restaurant in building.restaurants.all():
        info += restaurant.kr_name+","
    if building.restaurants.count != 0:
        info += "\n"
    #cafes
    if building.cafes.count != 0:
        info += "카페:"
    for cafe in building.cafes.all():
        info += cafe.kr_name+","
    if building.cafes.count != 0:
        info += "\n"
    #convs
    if building.convs.count != 0:
        info += "편의점:"
    for conv in building.convs.all():
        info += conv.kr_name+","
    if building.convs.count != 0:
        info += "\n"
    #banks
    if building.banks.count != 0:
        info += "은행:"
    for bank in building.banks.all():
        info += bank.kr_name+","
    if building.banks.count != 0:
        info += "\n"
    #atms
    if building.atms.count != 0:
        info += "ATM:"
    for atm in building.atms.all():
        info += atm.kr_name+","
    if building.atms.count != 0:
        info += "\n"
    #done
    building.info = info
    building.save()