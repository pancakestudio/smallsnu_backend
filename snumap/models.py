from django.db import models

# Create your models here.

class Map(models.Model):
    link = models.URLField(max_length=200)

class Spot(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    map = models.ForeignKey(Map , related_name='spots', on_delete=models.CASCADE)

class Edge(models.Model):
    spots = models.ManyToManyField(Spot, related_name='edges')

class Shuttle(models.Model):
    kr_name = models.CharField(max_length=200)
    en_name = models.CharField(max_length=200)
    operating_hours = models.TextField()
    info = models.TextField()
    edges = models.ManyToManyField(Edge, related_name='shuttles')

class Route(models.Model):
    start = models.ForeignKey(Spot , related_name='start_for', on_delete=models.CASCADE)
    end = models.ForeignKey(Spot , related_name='end_for', on_delete=models.CASCADE)
    length = models.FloatField()
    edges = models.ManyToManyField(Edge)

class Building(models.Model):
    code = models.CharField(max_length=200)
    kr_name = models.CharField(max_length=200)
    en_name = models.CharField(max_length=200)
    spot = models.ForeignKey(Spot, related_name='building', on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    info = models.TextField()

class Restaurant(models.Model):
    location = models.CharField(max_length=200)
    kr_name = models.CharField(max_length=200)
    en_name = models.CharField(max_length=200)
    building = models.ForeignKey(Building, related_name='restaurants', on_delete=models.CASCADE)
    operating_hours = models.TextField()

class Cafe(models.Model):
    location = models.CharField(max_length=200)
    kr_name = models.CharField(max_length=200)
    en_name = models.CharField(max_length=200)
    building = models.ForeignKey(Building, related_name='cafes', on_delete=models.CASCADE)
    operating_hours = models.TextField()

class Conv(models.Model):
    location = models.CharField(max_length=200)
    kr_name = models.CharField(max_length=200)
    en_name = models.CharField(max_length=200)
    building = models.ForeignKey(Building, related_name='convs', on_delete=models.CASCADE)
    operating_hours = models.TextField()

class Bank(models.Model):
    location = models.CharField(max_length=200)
    kr_name = models.CharField(max_length=200)
    en_name = models.CharField(max_length=200)
    building = models.ForeignKey(Building, related_name='banks', on_delete=models.CASCADE)
    operating_hours = models.TextField()

class Atm(models.Model):
    location = models.CharField(max_length=200)
    kr_name = models.CharField(max_length=200)
    en_name = models.CharField(max_length=200)
    building = models.ForeignKey(Building, related_name='atms', on_delete=models.CASCADE)
    operating_hours = models.TextField()

class Seminar(models.Model):
    title = models.CharField(max_length=200)
    talker = models.TextField()
    description = models.TextField()
    building = models.ForeignKey(Building, related_name='seminars', on_delete=models.CASCADE)
    where = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    link = models.URLField(max_length=200)

class Lecture(models.Model):
    code = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    professor = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    building = models.ForeignKey(Building, related_name='lectures', on_delete=models.CASCADE)
    time = models.CharField(max_length=200)

class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    building = models.ForeignKey(Building, related_name='posts', on_delete=models.CASCADE)