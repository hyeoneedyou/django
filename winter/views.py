from django.shortcuts import render


def weather(request):
    return render(request, 'winter/weather.html')


def clear(request):
    return render(request, 'winter/clear.html')


def cloudy(request):
    return render(request, 'winter/cloudy.html')


def rain(request):
    return render(request, 'winter/rain.html')
