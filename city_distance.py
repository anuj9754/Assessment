from math import radians, cos, sin, asin, sqrt


class CalculateDistance:
    def __init__(self, city1, city2):
        self.city1 = city1
        self.city2 = city2

    def convert_lon_lat(self, latitude, longitude):
        latitude = sum(float(x) / 60 ** n for n, x in enumerate(latitude[:-1].split('-'))) * (
            1 if 'N' in latitude[-1] else -1)
        longitude = sum(float(x) / 60 ** n for n, x in enumerate(longitude[:-1].split('-'))) * (
            1 if 'E' in longitude[-1] else -1)
        return latitude, longitude

    def distance(self):
        city1_split = self.city1.split(',')
        city2_split = self.city2.split(',')
        # city 1 lon and lat
        lat1, lon1 = self.convert_lon_lat(city1_split[0], city1_split[1])

        # city2 lon and lat
        lat2, lon2 = self.convert_lon_lat(city2_split[0], city2_split[1])

        lon1 = radians(lon1)
        lon2 = radians(lon2)
        lat1 = radians(lat1)
        lat2 = radians(lat2)

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

        c = 2 * asin(sqrt(a))

        # Radius of earth in kilometers
        r = 6371

        # calculate the result
        return round((c * r), 2)


if __name__ == '__main__':
    city1 = input("City1 :- ")
    city2 = input("City2 :- ")
    obj = CalculateDistance(city1, city2)
    print(obj.distance(), "K.M")
