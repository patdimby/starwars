from .views import *
from django.urls import path

urlpatterns = [
    path("root/", RootList.as_view()),
    path("test/", test , name="test"),
    path("people/", PeopleList.as_view(), name="people_list"), # people
    path("people/<int:id>/", PeopleDetail.as_view(), name="people_detail"),
    path("films/", FilmsList.as_view()), # film
    path("films/<int:id>/", FilmsDetail.as_view()),
    path("starships/", StarshipsList.as_view()), # starships
    path("starships/<int:id>/", StarshipsDetail.as_view()),
    path("vehicles/", VehiclesList.as_view()), # vehicles
    path("vehicles/<int:id>/", VehiclesDetail.as_view()),
    path("species/", SpeciesList.as_view()), # species
    path("species/<int:id>/", SpeciesDetail.as_view()),
    path("planets/", PlanetsList.as_view()), # planets
    path("planets/<int:id>/", PlanetsDetail.as_view()),
]
