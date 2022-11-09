import math

from utils import *

if __name__ == '__main__':
    file_path = Path("attendee_locations.csv")
    city_collection = read_attendees_file(file_path)
    city_collection.countries()
    city_collection.total_attendees()

    zurich = City('Beijing', 'China', 52, 39.90, 116.39)
    san_francisco = City('Nanning', 'China', 71, 32.06, 118.79)
    list_of_cities = [zurich, san_francisco]
    city_collection1 = CityCollection(list_of_cities)
    distance = zurich.distance_to(san_francisco)
    print(distance)







