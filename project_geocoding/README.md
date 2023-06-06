# Geocoding Addresses 🌍🔍✉️

This script retrieves latitude and longitude coordinates for a given address using the Nominatim geocoding service. It takes input addresses from a CSV file, geocodes them, and saves the results back to the same file.

## Prerequisites

- Python 3.x
- `geopy` library: Install it using `pip install geopy`
- `pandas` library: Install it using `pip install pandas`

## Usage

1. Make sure you have the necessary libraries installed.
2. Create a CSV file named `address.csv` containing the addresses you want to geocode. The file should have a column named "Address" that contains the addresses.
3. Open the script file (`geocoding_script.py`).
4. Set the `filename` variable to the name of your CSV file (if different from `address.csv`).
5. Set the `country_codes` variable to the two-letter country code(s) (optionally).
6. Run the script by executing the following command: `python geocoding_script.py`
7. You can find the geocoded coordinates in a new column named "Coordinates" in the CSV file.

**Note:** The script includes a `get_coordinates_and_sleep` function that pauses the execution for 1 second after each geocoding request to prevent potential IP blocking. If you don't need this delay, you can modify the code to use the `get_coordinates` function directly.

## Disclaimer

The script uses the Nominatim geocoding service provided by OpenStreetMap. Please review their [usage policy](https://operations.osmfoundation.org/policies/nominatim/) and ensure compliance with the terms and conditions.
