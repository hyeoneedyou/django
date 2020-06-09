from django.shortcuts import render


def weather(request):
    return render(request, 'summer/weather.html')


def clear(request):
    return render(request, 'summer/clear.html')


def cloudy(request):
    return render(request, 'summer/cloudy.html')


def rain(request):
    return render(request, 'summer/rain.html')
