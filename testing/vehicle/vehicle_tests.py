from vehicle import Vehicle, Car, Truck
import unittest


class VehicleTests(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car(2, 1)
        self.truck = Truck(2, 1)

    def test_car_init_method(self):
        self.assertEqual(self.car.fuel_quantity, 2)
        self.assertEqual(self.car.fuel_consumption, 1)

    def test_truck_init_method(self):
        self.assertEqual(self.truck.fuel_quantity, 2)
        self.assertEqual(self.truck.fuel_consumption, 1)

    def test_refuel_car(self):
        self.car.refuel(1)
        self.assertEqual(self.car.fuel_quantity, 3)

    def test_refuel_truck(self):
        self.truck.refuel(8)
        self.assertEqual(self.truck.fuel_quantity, 9.6)

    def test_car_drive_enough_fuel(self):
        self.car.fuel_quantity = 1.9
        self.car.drive(1)
        self.assertEqual(self.car.fuel_quantity, 0)

    def test_car_drive_not_enough_fuel(self):
        self.car.drive(10)
        self.assertEqual(self.car.fuel_quantity, 2)

    def test_truck_drive_enough_fuel(self):
        self.truck.fuel_quantity = 2.6
        self.truck.drive(1)
        self.assertEqual(self.truck.fuel_quantity, 0)

    def test_truck_drive_not_enough_fuel(self):
        self.truck.drive(10)
        self.assertEqual(self.truck.fuel_quantity, 2)


if __name__ == "__main__":
    unittest.main()
