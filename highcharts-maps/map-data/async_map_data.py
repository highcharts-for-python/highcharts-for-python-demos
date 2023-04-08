from highcharts_maps.constants import EnforcedNull
from highcharts_maps.chart import Chart
import requests
import json

response = requests.get('https://cdn.jsdelivr.net/gh/highcharts/highcharts@c116b6fa6948448/samples/data/us-counties-unemployment.json')
data_as_str = response.text
data_as_obj = json.loads(data_as_str)

options = {
    'chart': {
        'map': 'https://code.highcharts.com/mapdata/countries/us/us-all-all.topo.json',
        'borderWidth': 1,
        'marginRight': 20
    },

    'title': {
        'text': 'US Counties unemployment rates, January 2018'
    },

    'accessibility': {
        'description': 'Demo showing a large dataset.'
    },

    'legend': {
        'layout': 'vertical',
        'align': 'right',
        'floating': True,
        'backgroundColor': 'rgba(255, 255, 255, 0.85)'
    },

    'mapNavigation': {
        'enabled': True
    },

    'colorAxis': {
        'min': 0,
        'max': 25,
        'tickInterval': 5,
        'stops': [[0, '#F1EEF6'], [0.65, '#900037'], [1, '#500007']],
        'labels': {
            'format': '{value}%'
        }
    },

    'plotOptions': {
        'mapline': {
            'showInLegend': False,
            'enableMouseTracking': False
        }
    },

    'series': [{
        'data': data_as_obj,
        'joinBy': ['hc-key', 'code'],
        'name': 'Unemployment rate',
        'tooltip': {
            'valueSuffix': '%'
        },
        'borderWidth': 0.5,
        'states': {
            'hover': {
                'color': '#a4edba'
            }
        },
        'shadow': False,
        'accessibility': {
            'enabled': False
        },
        'type': 'map'
    }, {
        'type': 'mapline',
        'name': 'State borders',
        'color': 'white',
        'shadow': False,
        'borderWidth': 2,
        'accessibility': {
            'enabled': False
        }
    }]
}

chart = Chart.from_options(options)
chart.is_maps_chart = True

chart.display()