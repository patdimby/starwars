# starwarstasks/tests.py
from django.test import TestCase
from django.urls import reverse 
from rest_framework import status 
from rest_framework.test import APITestCase 
from .models import People

class TodoModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.people = People.objects.create(
        name = "C-3PO", 
        birth_year = "112BBY",
        eye_color = "yellow",
        gender ="Male",
        hair_color ="Transparent",
        height ="300",
        mass ="20",
        skin_color ="violet",
        homeworld ="http://planet",
        url ="http://media",
        created = "26/02/2023 00:00",
        edited = "26/02/2023 00:00"
    )
    
    def test_people_content(self):
        self.assertEqual(self.people.name, "C-3PO")
        self.assertEqual(self.people.birth_year, "112BBY")
        self.assertEqual(str(self.people), "C-3PO")

    def test_people_listview(self): 
        response = self.client.get(reverse("people_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(People.objects.count(), 1)
        self.assertContains(response, self.people)
        
    def test_people_detailview(self):
        response = self.client.get(
        reverse("people_detail", kwargs={"id": self.people.id}),format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(People.objects.count(), 1)
        self.assertContains(response, "Luke Skywalker")