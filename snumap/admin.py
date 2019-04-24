from django.contrib import admin
from .models import Map, Spot, Edge, Shuttle, Route, Building, Restaurant, Seminar, Lecture, Post
# Register your models here.

admin.site.register([Map, Spot, Edge, Shuttle, Route, Building, Restaurant, Seminar, Lecture, Post])