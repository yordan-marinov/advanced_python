from cat import Cat

import unittest


class CatTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Jordan")

    def test_correct_name_upon_init(self):
        self.assertEqual(self.cat.name, "Jordan")

    def test_eat_method_raise_exception_if_cat_fed(self):
        self.cat.fed = True
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_increase_size_after_eat_by_one(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_is_fed_after_eat(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_after_fed_cat_raise_error(self):
        self.cat.fed = True
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_cannot_sleep_if_not_fed(self):
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat_not_sleepy_after_sleep_method(self):
        self.cat.eat()
        # self.cat.sleepy = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    unittest.main()
