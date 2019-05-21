from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('map/', views.map_list),
    path('building/', views.building_list),
    path('building/<pk>/', views.building_detail),
    path('building/<pk>/post/', views.building_post),
    path('building/<pk>/restaurant/', views.building_restaurant),
    path('building/<pk>/seminar/', views.building_seminar),
    path('post/<int:postId>/', views.building_post_detail),
    path('post/', views.post_list),
    path('seminar/', views.seminar_list),
    path('seminar/<int:pk>/', views.seminar_detail),
    path('restaurant/', views.restaurant_list),
    path('restaurant/<int:pk>/', views.restaurant_detail),
    path('shuttle/', views.shuttle_list),
    path('lecture/', views.lecture_list),
    path('lecture/<int:pk>/', views.lecture_detail),
    path('route/', views.route_list),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

urlpatterns = format_suffix_patterns(urlpatterns)