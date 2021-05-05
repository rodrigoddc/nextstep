from django.urls import path
from .api import PersonCreateApi, PersonListApi, PersonUpdateApi, PersonGetApi

app_name = 'core'
urlpatterns = [
    path('persons/', PersonListApi.as_view(), name='list'),
    path('persons/create/', PersonCreateApi.as_view(), name='create'),
    path('persons/<int:pk>/detail/', PersonGetApi.as_view(), name='detail'),
    path('persons/<int:pk>/update', PersonUpdateApi.as_view(), name='update'),
    path('persons/<int:pk>/delete', PersonUpdateApi.as_view(), name='delete'),
]