from typing import Dict, List, Tuple
import utils
from math import *


class City:

    def __init__(self, city_name, country, citizen_num, latitude, longitude):

        def is_num(n):
            try:
                n = eval(n)
                if type(n) == int or type(n) == float or type(n) == complex:
                    return True
            except Exception as e:
                raise utils.DecimalException('The latitude or longitude is not decimal number')

        if city_name == '' or not isinstance(city_name, str):
            raise ValueError('The name is empty or not string')
        if country == '' or not isinstance(country, str):
            raise ValueError('The country is empty or not string')
        if not isinstance(citizen_num, int) or citizen_num <= 0:
            raise ValueError('The citizen number is not integer or invalid')
        if not is_num(str(latitude)):
            pass
        if not is_num(str(longitude)):
            pass
        if float(latitude) > 90 or float(latitude) < -90:
            raise ValueError('The latitude should be restricted to the -90 to 90')
        if float(longitude) > 180 or float(latitude) < -180:
            raise ValueError('The latitude should be restricted to the -180 to 180')
        self.city_name = city_name
        self.country = country
        self.citizen_num = citizen_num
        self.latitude = latitude
        self.longitude = longitude

    def distance_to(self, other: 'City') -> float:
        r = 6371
        lon1, lat1, lon2, lat2 = map(radians, [self.longitude, self.latitude, other.longitude, other.latitude])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        d = c * r
        return float(d)

    def co2_to(self, other: 'City') -> float:
        raise NotImplementedError
    
    @staticmethod
    def method():
        print('我是静态方法')
    
    @classmethod
    def clsmethod(cls):
        print('我是类方法')


class CityCollection:
    
    #csv_data = None

    def __init__(self, cities: City):
        self.cities = cities

    def countries(self) -> List[str]:
        temp_list = []
        countries_list = []
        for city in self.cities:
            temp_list.append(city.country)
        for x in temp_list:
            if x not in countries_list:
                countries_list.append(x)
        print(countries_list)


    def total_attendees(self) -> int:
        attendees_number = 0
        for city in self.cities:
            attendees_number += city.citizen_num
        print(attendees_number)


    def total_distance_travel_to(self, city: City) -> float:
        raise NotImplementedError

    def travel_by_country(self, city: City) -> Dict[str, float]:
        raise NotImplementedError

    def total_co2(self, city: City) -> float:
        raise NotImplementedError

    def co2_by_country(self, city: City) -> Dict[str, float]:
        raise NotImplementedError

    def summary(self, city: City):
        raise NotImplementedError

    def sorted_by_emissions(self) -> List[Tuple[str, float]]:
        raise NotImplementedError

    def plot_top_emitters(self, city: City, n: int, save: bool):
        raise NotImplementedError


    # @property
    # def name(self):
    #     return self._name
    #
    # @property
    # def country(self):
    #     return self._country
    #
    # @property
    # def citizen_num(self):
    #     return self._citizen_num
    #
    # @property
    # def latitude(self):
    #     return self._latitude
    #
    # @property
    # def longitude(self):
    #     return self._longitude

    # name = property(operator.attrgetter('_name'))
    # country = property(operator.attrgetter('_country'))
    # citizen_num = property(operator.attrgetter('_citizen_num'))
    # latitude = property(operator.attrgetter('_latitude'))
    # longitude = property(operator.attrgetter('_longitude'))

    # @name.setter
    # def name(self, n):
    #     self._name = n
    #
    # @country.setter
    # def country(self, c):
    #     self._country = c
    #
    # @citizen_num.setter
    # def citizen_num(self, n):
    #     self._citizen_num = n
    #
    # @latitude.setter
    # def latitude(self, la):
    #     self._latitude = la
    #
    # @longitude.setter
    # def name(self, lo):
    #     self._longitude = lo


    # @name.getter
    # def name(self):
    #     return self._name
    #
    # @country.getter
    # def country(self):
    #     return self._country
    #
    # @citizen_num.getter
    # def citizen_num(self):
    #     return self._citizen_num
    #
    # @latitude.getter
    # def latitude(self):
    #     return self._latitude
    #
    # @longitude.getter
    # def name(self):
    #     return self._longitude
