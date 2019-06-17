from snumap.models import Spot, Edge, Shuttle, Route
import json

spots = Spot.objects.all()
edges = Edge.objects.all()

v = spots.count()

dist = []
key = []
edgeId = []

# 100.0 for no possible route
for row in range(v+1):
    row = []
    for column in range(v+1):
        row.append(100.0)
    dist.append(row)

#-1 for no connection, 0 for direct connection
for row in range(v+1):
    row = []
    for column in range(v+1):
        row.append(-1)
    key.append(row)

#-1 for no edge
for row in range(v+1):
    row = []
    for column in range(v+1):
        row.append(-1)
    edgeId.append(row)


for edge in edges:
    edgeSpots = edge.spots.all()
    start = edgeSpots[0].id
    end = edgeSpots[1].id
    length = edge.length
    dist[start][end] = length
    key[start][end] = 0
    edgeId[start][end]=edge.id
    dist[end][start] = length
    key[end][start] = 0
    edgeId[end][start]=edge.id

for i in range(v+1):
    dist[i][i] = 0.0

for k in range(v+1):
    for i in range(v+1):
        for j in range(v+1):
            if dist[i][j] > (dist[i][k]+dist[k][j]):
                key[i][j] = k
                dist[i][j] = (dist[i][k]+dist[k][j])

#indexing by spotId itself
with open('dist.json', 'w', encoding="utf-8") as make_file:
    json.dump(dist, make_file, ensure_ascii=False, indent=4)

#indexing by spotId itself
with open('key.json', 'w', encoding="utf-8") as make_file:
    json.dump(key, make_file, ensure_ascii=False, indent=4)

#indexing by spotId itself
with open('edgeId.json', 'w', encoding="utf-8") as make_file:
    json.dump(edgeId, make_file, ensure_ascii=False, indent=4)


# USED FOR SAVING DATA AS ROUTE MODEL
# for i in range(size):
#     for j in range(size):
#         path = [i+1] + findPath(i, j, key)
#         start=Spot.objects.get(pk=(i+1))
#         end=Spot.objects.get(pk=(j+1))
#         route = Route(
#             start=start,
#             end=end,
#             length=float(dist[i][j])
#         )
#         route.save()
#         for step in range(len(path)-1):
#             edge = Edge.objects.get(pk=edgeId[path[step]][path[step+1]])
#             route.edges.add(edge)
#         route.save()