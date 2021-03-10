from solution import Person
import unittest


class solutionTests(unittest.TestCase):
    def setUp(self):
        self.person_child = Person("Martin", "Yordanov", 4, "boy", "Gabrovo")

    def tearDown(self):
        self.person_child = None

    def test_correct_initialization_with_all_properties(self):
        self.assertEqual(self.person_child.name, "Martin")
        self.assertEqual(self.person_child.last_name, "Yordanov")
        self.assertEqual(self.person_child.full_name, "Martin Yordanov")
        self.assertEqual(self.person_child.age, 4)
        self.assertEqual(self.person_child.gender, "boy")
        self.assertEqual(self.person_child.town, "Gabrovo")

    def test_get_info_returns_correct_output(self):
        expected = self.person_child.get_info()
        correct_return = 'Hi I am boy from Gabrovo on 4 and my name is Martin Yordanov!'
        self.assertEqual(expected, correct_return)
        
        
        
if __name__ == "__main__":
    unittest.main()