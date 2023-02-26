
from rest_framework import serializers

from .models import *


class RootSerializer(serializers.ModelSerializer):
    class Meta:
        model = Root
        fields = ["name","url"]

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields =  ['name','birth_year','eye_color','gender','hair_color', 'height','mass','skin_color','homeworld','url','created','edited',]

   

