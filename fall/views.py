from django.shortcuts import render


def weather(request):
    return render(request, 'fall/weather.html')



def clear(request):
    return render(request, 'fall/clear.html')


def cloudy(request):
    return render(request, 'fall/cloudy.html')


def rain(request):
    return render(request, 'fall/rain.html')