import requests
import time

def get_noaa_data(station_id, begin_date, end_date, product):
    """
    Fetch data from NOAA CO-OPS API.
    product can be 'wind', 'water_level', 'hourly_height'
    """
    url = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"
    params = {
        "begin_date": begin_date,
        "end_date": end_date,
        "station": station_id,
        "product": product,
        "datum": "MLLW",
        "units": "metric",
        "time_zone": "gmt",
        "application": "VisTrails_Benchmark",
        "format": "json"
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

def main():
    station_id = "8454000" # Providence, RI
    begin_date = "20230101"
    end_date = "20230102"
    
    start_time = time.time()
    
    print("Fetching wind data...")
    wind_data = get_noaa_data(station_id, begin_date, end_date, "wind")
    if wind_data and 'data' in wind_data:
        print(f"Retrieved {len(wind_data['data'])} wind records.")
    
    print("Fetching hourly water level data...")
    water_level_data = get_noaa_data(station_id, begin_date, end_date, "hourly_height")
    if water_level_data and 'data' in water_level_data:
        print(f"Retrieved {len(water_level_data['data'])} water level records.")
        
    end_time = time.time()
    print(f"NOAA API calls completed in {end_time - start_time:.4f} seconds")

if __name__ == '__main__':
    main()
