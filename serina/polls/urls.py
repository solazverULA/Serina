from django.urls import path, include
from polls import views
#se importan todas las urls de la vista de polls

#app_name = 'polls'
urlpatterns = [
    path('', views.index, name ='index'),
]
