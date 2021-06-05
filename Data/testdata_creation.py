"""
Module for creating test data for (parameterize)
"""
import json
from Library.config import Config

data = {
    'TD1':{'Email':'email2thisid@gmail.com',
           'Password':'password',
           'Song':'Lahore',
           'Playlist':'So Fresh: Tamil',
           'Track':'Enjoy Enjammi',
           'Label':'Label: 2021 maajja',
           'Music':'Dhee,Arivu,Santhosh Narayanan',
           'Artist':'Dhee,Arivu,Santhosh Narayanan',
           'Lyricist':'Arivu'
           },
    'TD2': {'Email': 'email2thisid1@gmail.com',
            'Password': 'password1',
            'Song': 'Suicide',
            'Playlist': 'So Fresh: Tamil',
            'Track': 'Inna Mylu',
            'Label': 'Label: Think Music',
            'Music': 'Nishanth',
            'Artist': 'Kamala Kannan,Sivakarthikeyan,Poovaiyar,Rajesh,Britto michael',
            'Lyricist': 'N/A'
            }
}

with open(Config.TEST_JSON, 'w+') as fileobj:
    json.dump(data, fileobj, indent=4)
