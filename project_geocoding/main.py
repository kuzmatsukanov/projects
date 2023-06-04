from geopy.geocoders import Nominatim
import time
import pandas as pd


def get_coordinates(address, country_codes=None):
    """
    Retrieve the latitude and longitude coordinates for a given address.

    Parameters:
    - address (str): The address for which coordinates are to be retrieved.
    - country_codes (str or list): Two-letter country codes to bias the search towards specific countries.
      Defaults to None. E.g. 'PK'

    Returns:
    - tuple: A tuple containing the latitude and longitude coordinates of the given address.
             Returns None if the address cannot be geocoded. E.g. (37.422035, -122.084124)
    """
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(address, country_codes=country_codes)
    if location:
        return location.latitude, location.longitude
    else:
        return None


def get_coordinates_and_sleep(address, country_codes=None):
    """
    Retrieve the latitude and longitude coordinates for a given address.
    Pauses the execution for 1 second after retrieving the coordinates to prevent potential IP blocking.

    Parameters:
    - address (str): The address for which coordinates are to be retrieved.
    - country_codes (str or list): Two-letter country codes to bias the search towards specific countries.
      Defaults to None. E.g. 'PK'

    Returns:
    - tuple: A tuple containing the latitude and longitude coordinates of the given address.
             Returns None if the address cannot be geocoded. E.g. (37.422035, -122.084124)
    """
    get_coordinates(address, country_codes)
    time.sleep(1)
    return


def main():
    """Converts address to coordinates"""
    filename = 'address.csv'
    country_codes = 'PK'
    df = pd.read_csv(filename)
    df['Coordinates'] = df['Address'].apply(lambda x: get_coordinates_and_sleep(x, country_codes))
    df.to_csv(filename, index=False)


if __name__ == "__main__":
    main()
