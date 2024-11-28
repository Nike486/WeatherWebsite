import json
from datetime import datetime

today = datetime.now()
formatted_date = today.strftime('%d.%m')

def parse_time(dt_txt):
    dt_object = datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S')
    return dt_object.strftime('%H:%M')

def parse_date(dt_txt):
    dt_object = datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S')
    return dt_object.strftime('%d.%m')

def parse_icon(dt_txt):
    priority = {
        "11d": 1,
        "11n": 2,

        "09d": 3,
        "09n": 4,

        "10d": 5,
        "10n": 6,

        "13d": 7,
        "13n": 8,

        "50d": 9,
        "50n": 10,

        "04d": 11,
        "04n": 12,

        "03d": 13,
        "03n": 14,

        "02d": 15,
        "02n": 16,

        "01d": 17,
        "01n": 18
    }

    priority_icon  = None
    priority_value = float('inf')

    for icon in dt_txt:
        if priority[icon] < priority_value:
            priority_value = priority[icon]
            priority_icon = icon

    return priority_icon

def parse_json(json_file):
    data = json_file
    time = []
    date_tamp = []

    for item in data['list']:
        temp   = item['main']['temp']
        dt_txt = item['dt_txt']
        icon   = item['weather'][0]['icon']

        time.append({
            'time': parse_time(dt_txt),
            'temperature': temp,
            'icon': icon
        })

        cor_date = parse_date(dt_txt)
        if cor_date != formatted_date:
            date_tamp.append({
                'date': cor_date,
                'temperature': temp,
                'icon': icon
            })

    time = time[:6]

    temperature_data = {}

    for entry in date_tamp:
        date = entry['date']
        temp = entry['temperature']
        icon = entry['icon']

        if date not in temperature_data:
            temperature_data[date] = {'total_temp': 0, 'count': 0, 'icon': []}

        temperature_data[date]['total_temp'] += temp
        temperature_data[date]['count'] += 1
        temperature_data[date]['icon'].append(icon)

    average_temperatures = []
    for date, values in temperature_data.items():
        average_temperatures.append({
            'date': date,
            'temperature': round(values['total_temp'] / values['count'], 2),
            'icon': parse_icon(values['icon'])
        })

    result = {
        'city': data['city']['name'],
        'time': time,
        'average_temperatures': average_temperatures
    }

    return result