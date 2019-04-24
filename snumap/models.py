from django.db import models

# Create your models here.

class Map(models.Model):
    link = models.URLField()

class Spot(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    map = models.ForeignKey(Map , related_name='spots', on_delete=models.CASCADE)

class Edge(models.Model):
    spots = models.ManyToManyField(Spot, related_name='edges')

class Shuttle(models.Model):
    kr_name = models.CharField()
    en_name = models.CharField()
    operating_hours = models.TextField()
    info = models.TextField()
    edges = models.ManyToManyField(Edge, related_name='shuttles')

class Route(models.Model):
    start = models.ForeignKey(Spot , on_delete=models.CASCADE)
    end = models.ForeignKey(Spot , on_delete=models.CASCADE)
    length = models.FloatField()
    edges = models.ManyToManyField(Edge)

class Building(models.Model):
    code = models.CharField()
    kr_name = models.CharField()
    en_name = models.CharField()
    spot = models.ForeignKey(Spot, related_name='building', on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    info = models.TextField()

class Restaurant(models.Model):
    code = models.CharField()
    kr_name = models.CharField()
    en_name = models.CharField()
    building = models.ForeignKey(Building, related_name='restaurants', on_delete=models.CASCADE)
    operating_hours = models.TextField()

class Seminar(models.Model):
    title = models.CharField()
    description = models.CharField()
    building = models.ForeignKey(Building, related_name='seminars', on_delete=models.CASCADE)
    time = models.CharField()

class Lecture(models.Model):
    code = models.CharField()
    title = models.CharField()
    professor = models.CharField()
    link = models.URLField()
    building = models.ForeignKey(Building, related_name='lectures', on_delete=models.CASCADE)
    time = models.CharField()

class Post(models.Model):
    title = models.CharField()
    content = models.TextField()
    username = models.CharField()
    password = models.CharField()
    building = models.ForeignKey(Building, related_name='posts', on_delete=models.CASCADE)