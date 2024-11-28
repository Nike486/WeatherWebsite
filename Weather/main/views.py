from django.shortcuts import render
from .getWeather import get_weather


def weather_view(request):
    city_name = request.GET.get('city', 'Тула')
    weather_data = get_weather(city_name)
    return render(request, 'main/weatherPage.html', {'weather_data': weather_data})