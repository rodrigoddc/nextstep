from rest_framework import generics
from rest_framework.response import Response
from .serializer import PersonSerializer
from .models import Person




class PersonCreateApi(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonListApi(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonGetApi(generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDeleteApi(generics.RetrieveUpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer