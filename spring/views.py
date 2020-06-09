from django.shortcuts import render


def weather(request):
    return render(request, 'spring/weather.html')


def clear(request):
    return render(request, 'spring/clear.html')


def cloudy(request):
    return render(request, 'spring/cloudy.html')


def rain(request):
    return render(request, 'spring/rain.html')



