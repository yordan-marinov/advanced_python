import unittest

from project.vehicle import Vehicle


class TestsVehicle(unittest.TestCase):
    def setUp(self):
        self.v = Vehicle(10.1, 100.1)

    def test_correct_initiolization_v(self):
        self.assertEqual(10.1, self.v.fuel)
        self.assertEqual(100.1, self.v.horse_power)
        self.assertEqual(10.1, self.v.capacity)
        self.assertEqual(1.25, self.v.fuel_consumption)

    def test_drive_when_fuel_not_enoght_raise_exeption_str(self):
        with self.assertRaises(Exception) as contex:
            self.v.drive(10)

        self.assertEqual("Not enough fuel", str(contex.exception))

    def test_drive_when_fuel_enoght_decreases_fuel_with_consuptuon_mul_kilometers(self):
        self.v.drive(1)
        self.assertEqual(8.85, self.v.fuel)

    def test_refuel_when_fuel_is_more_than_capacity_raises_exeption(self):
        with self.assertRaises(Exception) as contex:
            self.v.refuel(10.2)

        self.assertEqual("Too much fuel", str(contex.exception))

    def test_refuel_when_fuel_is_less_than_capacity_add_given_quantity_to_fuel(self):
        self.v.drive(1)
        self.v.refuel(1.25)
        self.assertEqual(10.1, self.v.fuel)

    def test_correct__str__rerpresantation(self):
        expected = (
            f"The vehicle has 100.1 "
            f"horse power with 10.1 fuel left and 1.25 "
            f"fuel consumption"
        )
        self.assertEqual(expected, str(self.v))


if __name__ == "__main__":
    unittest.main()