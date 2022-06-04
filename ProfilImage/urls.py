
from django.urls import path
from .views import (
    Home, SaveProfile
)

app_name = 'ProfilImage'
urlpatterns = [
    path('', Home),
    path('image_file/', SaveProfile, name='SubmitFile')
]
