import requests as r
import json
import time

url = 'http://IP/get?'  #url to retreive data from
what_to_get = ['magX', 'magY', 'magZ', 'mag']

def phyphox_data():
    try:
        #creating request URL
        full_url = url + '&'.join(what_to_get)
        response = r.get(full_url, timeout=5)  #Set a timeout to avoid hanging

        #Parse JSON response
        data = response.json()
        
        # Extract and print values
        for item in what_to_get:
            if item in data['buffer']:
                mag_data = data['buffer'][item]['buffer'][0]
                print(f'{item}: {mag_data:10.7}')
            else:
                print(f"{item} not found in response")

    except r.exceptions.RequestException as e:
        print(f"Error connecting to Phyphox: {e}")
    except (KeyError, json.JSONDecodeError):
        print("Invalid response. Ensure Phyphox is running and accessible.")

# Keep fetching data
while True:
    phyphox_data()
    time.sleep(0.1)

