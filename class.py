
class Driver:
    def __init__(self, driver_id, __name, _phone):
        self.driver_id = driver_id
        self.name = __name
        self.phone = phone



class Car:
    def __init__(self, car_id, driver_id, __model):
        self.car_id = car_id
        self.driver_id = driver_id
        self.model = __model


class Client:
    def __init__(self, client_id, __CLname):
        self.__id = client_id
        self.CLname = __CLname


class Location:
    def __init__(self, loc_id, __address):
        self.loc_id = loc_id
        self.address = __address


class Route:
    def __init__(self, route_id, loc_id, __destination):
        self.route_id = route_id
        self.loc_id = loc_id
        self.destination = __destination





class Order:
    def __init__(self, __order_id, driver_id, __name, __client_id, route_id, __price, __CLname):
        self.order_id = __order_id
        self.driver_id = driver_id
        self.name = __name
        self.client_id = __client_id
        self.CLname = __CLname
        self.route_id = route_id
        self.price = __price

