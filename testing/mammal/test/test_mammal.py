import unittest

from project.mammal import Mammal


class MammalTests(unittest.TestCase):
    name = "Jordan"
    mammal_type = "Bear"
    sound = "Roar"

    def setUp(self):
        self.m = Mammal(self.name, self.mammal_type, self.sound)

    def test_correct_initiolization_mammal(self):
        self.assertEqual(self.name, self.m.name)
        self.assertEqual(self.mammal_type, self.m.type)
        self.assertEqual(self.sound, self.m.sound)
        self.assertEqual("animals", self.m._Mammal__kingdom)

    def test_make_sound_correct_returt_string(self):
        self.assertEqual(f"{self.name} makes {self.sound}", self.m.make_sound())

    def test_get_kingdom_correct_return_privite_property__kingdom(self):
        self.assertEqual("animals", self.m.get_kingdom())

    def test_info_correct_return_of_string_info(self):
        self.assertEqual(f"{self.name} is of type {self.mammal_type}", self.m.info())


if __name__ == "__main__":
    unittest.main()
