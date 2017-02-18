import csv
import numpy as np
from extract import Extractor


BASE = "http://www.mapdevelopers.com/what-county-am-i-in.php?address="

with open("stations.csv", 'r') as f:
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

extractor = Extractor()
with extractor:
    for row in station_data:
        station = row[2]
        url = BASE + station.replace(' ', '%20')
        extractor.get(url)
        idx = 3
        for key, value in ids.items():
            row[idx] = extractor.id_text(value)
            idx += 1

with open('stations_new.csv', 'wb') as f:
    np.savetxt(f, station_data, fmt='%s,%s,%s,%s,%s,%s,%s,%s', delimiter=",",
               header=(",".join(headers)), comments='')
