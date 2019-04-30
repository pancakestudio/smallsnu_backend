from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('map/', views.map_list),
    path('building/', views.building_list),
    path('building/<int:pk>/', views.building_detail),
    path('building/<int:pk>/post/', views.building_post),
    path('post/<int:postId>/', views.building_post_update),
    path('seminar/', views.seminar_list),
    path('restaurant/', views.restaurant_list),
    path('shuttle/', views.shuttle_list),
    path('lecture/', views.lecture_list),
    path('route/', views.route_list),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

urlpatterns = format_suffix_patterns(urlpatterns)