
from django.urls import path
from .views import (
    Home, SaveProfile, GetAllData
)

app_name = 'ProfilImage'
urlpatterns = [
    path('', Home),
    path('get_all/', GetAllData),
    path('image_file/', SaveProfile, name='SubmitFile')
]
