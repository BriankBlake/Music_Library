from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.songs_list),
    path("<int:pk>/", views.song_detail),
]
