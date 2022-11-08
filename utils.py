from cities import City, CityCollection
import csv
from pathlib import Path


def read_attendees_file(filepath: Path) -> CityCollection:
    #with open(Path) as data:
        #csv_data = csv.reader(data)
    #csv_data = csv.reader(open(Path))

    csv_data = csv.reader(open(filepath))
    headers = next(csv_data)
    city_collection = CityCollection(None)
    CityCollection.csv_data = csv_data

    return city_collection
    