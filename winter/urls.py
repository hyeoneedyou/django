from django.urls import path
from .views import weather, clear, cloudy, rain

app_name="winter"
urlpatterns = [
    path('weather/', weather, name="weather"),
    path('clear/', clear, name="clear"),
    path('cloudy/', cloudy, name="cloudy"),
    path('rain/', rain, name="rain"),
]
