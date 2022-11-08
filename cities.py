import operator
from typing import Dict, List, Tuple

class DecimalException(Exception):
    def __init__(self, message):
        self.message = message

class City:

    def __init__(self, name, country, citizen_num, latitude, longitude):

        def isNum(n):
            try:
                n = eval(n)
                if type(n) == int or type(n) == float or type(n) == complex:
                    return True
            except Exception as e:
                raise DecimalException('The latitude or longitude is not decimal number')

        if name == '' or not isinstance(name, str):
            raise ValueError('The name is empty or not string')
        if country == '' or not isinstance(country, str):
            raise ValueError('The country is empty or not string')
        if not isinstance(citizen_num, int):
            raise ValueError('The citizen number is not integer')
        if not isNum(str(latitude)):
            pass
        if not isNum(str(longitude)):
            pass
        self.name = name
        self.country = country
        self.citizen_num = citizen_num
        self.latitude = latitude
        self.longitude = longitude

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



    def distance_to(self, other: 'City') -> float:
        raise NotImplementedError

    def co2_to(self, other: 'City') -> float:
        raise NotImplementedError
    
    @staticmethod
    def method():
        print('我是静态方法')
    
    @classmethod
    def clsmethod(cls):
        print('我是类方法')


class CityCollection:
    
    csv_data = None

    def __init__(self, cities: City):
        self.cities = cities

    def countries(self) -> List[str]:
        temp_list = []
        countries_list = []
        for row in CityCollection.csv_data:
            temp_list.append(row[1])
        for x in temp_list:
            if x not in countries_list:
                countries_list.append(x)
        print(countries_list)

    def total_attendees(self) -> int:
        attendees_number = 0
        for row in CityCollection.csv_data:
            attendees_number += 1
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


