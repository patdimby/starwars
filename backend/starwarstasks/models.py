from django.db import models
from typing import List
import datetime
import django.utils.timezone



# Create your models here.
class Root(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=255)  

    def __init__(self, i, name, url):
        self.id = i
        self.name = str(name)
        self.url = str(url)
    
    def __str__(self):
        return f"{self.id}, {self.name}, {self.url}"

class People(models.Model):
    name = models.CharField(max_length=255, default='', blank=True)  
    birth_year = models.CharField(max_length=255, default='', blank=True)    
    eye_color = models.CharField(max_length=255, default='', blank=True)    
    gender = models.CharField(max_length=255, default='', blank=True)   
    hair_color  = models.CharField(max_length=255, default='', blank=True)    
    height = models.CharField(max_length=255, default='', blank=True)  
    mass  = models.CharField(max_length=255, default='', blank=True)    
    skin_color  = models.CharField(max_length=255, default='', blank=True)   
    homeworld  = models.CharField(max_length=255, default='', blank=True)   
    url  = models.CharField(max_length=255, default='', blank=True)    
    created  = models.CharField(max_length=255, default='', blank=True)    
    edited  = models.CharField(max_length=255, default='', blank=True)  

    # films : List[str] # An array of film resource URLs that this person has been in.
    # species : List[str] # An array of species resource URLs that this person belongs to.
    # starships : List[str] # An array of starship resource URLs that this person has piloted.
    # vehicles : List[str] # An array of vehicle resource URLs that this person has piloted.

    def __str__(self):
        return self.name

class Film(models.Model):
    title = models.CharField(max_length=255, default='', blank=True)  
    episode_id = models.CharField(max_length=255, default='', blank=True)  
    opening_crawl = models.CharField(max_length=255, default='', blank=True)  
    director = models.CharField(max_length=255, default='', blank=True)  
    producer = models.CharField(max_length=255, default='', blank=True)  
    release_date= models.DateField(default=django.utils.timezone.now)

    url = models.CharField(max_length=255, default='', blank=True)  
    created = models.CharField(max_length=255, default='', blank=True)  
    edited = models.CharField(max_length=255, default='', blank=True)  

    # species  : List[str] # An array of species resource URLs that are in this film.
    # starships : List[str] # An array of starship resource URLs that are in this film.
    # vehicles : List[str] # An array of vehicle resource URLs that are in this film.
    # characters  : List[str] # An array of people resource URLs that are in this film.
    # planets : List[str] # An array of planet resource URLs that are in this film.

    