import csv
import numpy as np
from extract import Extractor


BASE = "http://www.mapdevelopers.com/what-county-am-i-in.php?address="

with open("stations_new.csv", 'r') as f:
    station_raw = list(csv.reader(f, delimiter=','))

    headers = station_raw[0]
    station_data = np.array(station_raw[1:])

ids = {
    'city': 'display_city',
    'county': 'display_county',
    'zipcode': 'display_zip',
    'latitude': 'display_lat',
    'longitude': 'display_lng'
}

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


extractor = Extractor()
with extractor:
    for row in station_data:
        # state = states[row[1]]
        station = row[2] # + " " + state
        url = BASE + station.replace(' ', '%20')
        if row[6] != '': 
            # skip if data already loaded
            print('PASS : ', row[:3])
        else:
            try:
                extractor.get(url)
                idx = 3
                for key, value in ids.items():
                    row[idx] = extractor.id_text(value)
                    idx += 1
                print('SUCC : ', row)
            except:
                print('ERR  : ',row[:3])
                extractor.reinitialize()
                # break 

with open('stations_new.csv', 'wb') as f:
    np.savetxt(f, station_data, fmt='%s,%s,%s,%s,%s,%s,%s,%s', delimiter=",",
               header=(",".join(headers)), comments='')

