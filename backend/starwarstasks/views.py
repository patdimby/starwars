from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import requests
from .models import *


from .models import *
from .serializers import *
from django.http import JsonResponse

base_url: str = "https://swapi.dev/api/"

# Create your views here.

# root
def test(request):   
    response = requests.get(base_url)
    data = response.json()    
    return JsonResponse(data, safe=False)

def set_path(url):
    response = requests.get(url)
    data = response.json()
    return data

def get_path(url):   
    response = requests.get(url)
    data = response.json()    
    return data


def set_root():
    response = requests.get(base_url)
    root = response.json()
    object_list = list()
    for i, (name, url) in enumerate(root.items()): 
        elt = Root(i, name, url)
        object_list.append(elt)
    return object_list


class RootList(APIView):
    """The Root resource provides information on 
    all available resources within the API."""
    permission_classes = (permissions.AllowAny,) 

    def get(self, request):
        result = set_root()  
        serializer = RootSerializer(result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    

# people
class PeopleList(APIView):
    """ get all the people resources """
    permission_classes = (permissions.AllowAny,)
    

    def __init__(self):
        self.url = base_url + "people/"

    def get(self, request):        
        response = get_path(self.url)
        return Response(response, status=status.HTTP_200_OK)
    

class PeopleDetail(APIView):
    """ get a specific people resource """
    permission_classes = (permissions.AllowAny,)
    
    def __init__(self):
        self.url = base_url + "people/"

    def get(self, request, id):        
        if id is not None:
            self.url += str(id)           
            response = get_path(self.url)
            if response.get("detail") is not None:
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(response, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# films. A Film resource is a single film.
class FilmsList(APIView):
    """ get all the film resources """
    permission_classes = (permissions.AllowAny,)
    

    def __init__(self):
        self.url = base_url + "films/"

    def get(self, request):        
        response = get_path(self.url)
        return Response(response, status=status.HTTP_200_OK)
    

class FilmsDetail(APIView):
    """ get a specific film resource """
    permission_classes = (permissions.AllowAny,)
    
    def __init__(self):
        self.url = base_url + "films/"

    def get(self, request, id):        
        if id is not None:
            self.url += str(id)           
            response = get_path(self.url)
            if response.get("detail") is not None:
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(response, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# starships - A Starship resource is a single transport craft that has hyperdrive capability.
class StarshipsList(APIView):
    """ get all the starship resources """
    permission_classes = (permissions.AllowAny,)
    

    def __init__(self):
        self.url = base_url + "starships/"

    def get(self, request):        
        response = get_path(self.url)
        return Response(response, status=status.HTTP_200_OK)
    

class StarshipsDetail(APIView):
    """ get a specific starship resource """
    permission_classes = (permissions.AllowAny,)
    
    def __init__(self):
        self.url = base_url + "starships/"

    def get(self, request, id):        
        if id is not None:
            self.url += str(id)           
            response = get_path(self.url)
            if response.get("detail") is not None:
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(response, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
# vehicles - A Vehicle resource is a single transport craft that does not have hyperdrive capability.
class VehiclesList(APIView):
    """ get all the vehicle resources """
    permission_classes = (permissions.AllowAny,)
    

    def __init__(self):
        self.url = base_url + "vehicles/"

    def get(self, request):        
        response = get_path(self.url)
        return Response(response, status=status.HTTP_200_OK)
    

class VehiclesDetail(APIView):
    """ get a specific vehicle resource """
    permission_classes = (permissions.AllowAny,)
    
    def __init__(self):
        self.url = base_url + "vehicles/"

    def get(self, request, id):        
        if id is not None:
            self.url += str(id)           
            response = get_path(self.url)
            if response.get("detail") is not None:
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(response, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# species - A Species resource is a type of person or character within the Star Wars Universe.
class SpeciesList(APIView):
    """ get all the species resources """
    permission_classes = (permissions.AllowAny,)
    

    def __init__(self):
        self.url = base_url + "species/"

    def get(self, request):        
        response = get_path(self.url)
        return Response(response, status=status.HTTP_200_OK)
    

class SpeciesDetail(APIView):
    """ get a specific specie resource """
    permission_classes = (permissions.AllowAny,)
    
    def __init__(self):
        self.url = base_url + "species/"

    def get(self, request, id):        
        if id is not None:
            self.url += str(id)           
            response = get_path(self.url)
            if response.get("detail") is not None:
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(response, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# planets
class PlanetsList(APIView):
    """ get all the planets resources """
    permission_classes = (permissions.AllowAny,)
    

    def __init__(self):
        self.url = base_url + "planets/"

    def get(self, request):        
        response = get_path(self.url)
        return Response(response, status=status.HTTP_200_OK)
    

class PlanetsDetail(APIView):
    """ get a specific planet resource """
    permission_classes = (permissions.AllowAny,)
    
    def __init__(self):
        self.url = base_url + "planets/"

    def get(self, request, id):        
        if id is not None:
            self.url += str(id)           
            response = get_path(self.url)
            if response.get("detail") is not None:
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(response, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
