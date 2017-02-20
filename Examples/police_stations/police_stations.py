import csv
import numpy as np
from extractor import Extractor


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
                extractor.driver.quit()
                extractor.reinitialize()
                # break 

with open('stations_complete.csv', 'wb') as f:
    np.savetxt(f, station_data, fmt='%s,%s,%s,%s,%s,%s,%s,%s', delimiter=",",
               header=(",".join(headers)), comments='')

