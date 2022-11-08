from utils import *

if __name__ == '__main__':
    file_path = Path("attendee_locations.csv")
    city_collection = read_attendees_file(file_path)
    #city_collection.countries()
    city_collection.total_attendees()

    zurich = City('Zurich', 'Switzerland', 52, 45.4, 8.33)
    print(zurich)
    san_fransciso = City('San Franciso', 'United States', 71, 33.77, -122.41)
    list_of_cities = [zurich, san_fransciso]
    city_collection1 = CityCollection(list_of_cities)
    print(city_collection1.cities == list_of_cities)



