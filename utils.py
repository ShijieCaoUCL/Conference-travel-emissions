from cities import City, CityCollection
import csv
from pathlib import Path


class DecimalException(Exception):
    def __init__(self, message):
        self.message = message


def read_attendees_file(filepath: Path) -> CityCollection:
    csv_data = csv.reader(open(filepath))
    headers = next(csv_data)
    list_of_cities = []
    for row in csv_data:
        city = City(row[3], row[1], int(row[0]), float(row[4]), float(row[4]))
        list_of_cities.append(city)

    city_collection = CityCollection(list_of_cities)

    return city_collection
