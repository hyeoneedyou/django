from django.urls import path
from .views import weather, clear, cloudy, rain

app_name="summer"
urlpatterns = [
    path('weather/', weather, name="weather"),
    path('clear/', clear, name="clear"),
    path('cloudy/', cloudy, name="cloudy"),
    path('rain/', rain, name="rain"),
]
