from car_manager import Car
import unittest


class CarTests(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car("name", "model", 1, 3)

    def test_init_method(self):
        self.assertEqual(self.car.make, "name")
        self.assertEqual(self.car.model, "model")
        self.assertEqual(self.car.fuel_consumption, 1)
        self.assertEqual(self.car.fuel_capacity, 3)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make_setter_empty_str_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.make = ""
        self.assertEqual(str(context.exception), "Make cannot be null or empty!")

    def test_make_setter_correct_str(self):
        self.car.make = "a"
        self.assertEqual(self.car.make, "a")

    def test_model_setter_empty_str_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.model = ""
        self.assertEqual(str(context.exception), "Model cannot be null or empty!")

    def test_model_setter_correct_str(self):
        self.car.model = "a"
        self.assertEqual(self.car.model, "a")

    def test_fuel_consumption_zero_value(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = 0
        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_consumption_negative_value(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = -1
        self.assertEqual(str(context.exception), "Fuel consumption cannot be zero or negative!")

    def test_correct_fuel_consumption_value(self):
        self.car.fuel_consumption = 2
        self.assertEqual(self.car.fuel_consumption, 2)

    def test_fuel_capacity_zero_value(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = 0
        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_capacity_negative_value(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = -1
        self.assertEqual(str(context.exception), "Fuel capacity cannot be zero or negative!")

    def test_correct_fuel_capacity_value(self):
        self.car.fuel_capacity = 2
        self.assertEqual(self.car.fuel_capacity, 2)

    def test_fuel_amount_negative_value(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -1
        self.assertEqual(str(context.exception), "Fuel amount cannot be negative!")

    def test_fuel_amount_correct_value(self):
        self.car.fuel_amount = 1
        self.assertEqual(self.car.fuel_amount, 1)

    def test_refuel_negative_zero_amount_fuel(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(0)
        self.assertEqual(str(context.exception), "Fuel amount cannot be zero or negative!")

    def test_max_refuel_amount_equal_capacity(self):
        self.car.refuel(100)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_refuel_amount_less_than_capacity(self):
        self.car.refuel(1)
        self.assertEqual(self.car.fuel_amount, 1)

    def test_drive_more_distance_than_fuel_raise_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.drive(1)
        self.assertEqual(str(context.exception), "You don't have enough fuel to drive!")

    def test_drive_distance_reduce_fuel_amount(self):
        self.car.refuel(1)
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount, 0)


if __name__ == "__main__":
    unittest.main()
