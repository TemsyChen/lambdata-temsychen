class Truck():

    def __init__(self, make, model, year, color, num_wheels):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.num_wheels = num_wheels

    def drive(self):
        print("we are driving", self.model)

if __name__ == '__main__':

    truck1 = Truck(make="Ford", model="F-350", year="2020", color="burnt orange", num_wheels="4")
    print(truck1.make)
    print(truck1.model)
    print(truck1.year)
    print(truck1.color)
    print(truck1.num_wheels)

class SUV():

    def __init__(self, make, model, year, color, num_wheels):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.num_wheels = num_wheels

if __name__ == '__main__':

    SUV1 = Truck(make="Ford", model="F-350", year="2020", color="burnt orange", num_wheels="4")
    print(SUV1.make)
    print(SUV1.model)
    print(SUV1.year)
    print(SUV1.color)
    print(SUV1.num_wheels)


function: drive