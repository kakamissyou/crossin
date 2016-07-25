class Vehicle:
    def __int__(self, speed):
        self.speed = speed

    def drive(self, distance):
        print 'Need %f hours' % (distance / self.speed)


class Bike(Vehicle):
    pass


class car(Vehicle):
    def __init__(self, speed, fule):
        Vehicle.__int__(self, speed)
        self.fule = fule

    def drive(self, distance):
        Vehicle.drive(self, distance)
        print 'Need %f fules' % (distance * self.fule)


b = Bike()
c = car(200, 0.12)
b.drive(100)
c.drive(100)
