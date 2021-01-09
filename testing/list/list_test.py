from list import IntegerList
import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.list = IntegerList()

    def test_add_correct_int_element_to_list(self):
        self.assertEqual(self.list.add(1), [1])

    def test_add_incorrect_type_to_list_raise_error(self):
        with self.assertRaises(ValueError) as context:
            self.list.add("1")
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_remove_index_operation_with_correct_index_return_element(self):
        self.list.add(1)
        self.list.add(2)
        self.list.add(3)
        element = self.list.remove_index(2)
        self.assertEqual(element, 3)

    def test_remove_correct_index_check_list_length(self):
        self.list.add(1)
        self.list.add(2)
        self.list.add(3)
        self.list.remove_index(0)
        self.assertEqual(self.list.get_data(), [2, 3])

    def test_remove_out_of_range_index_raises_index_error(self):
        self.list.add(1)
        self.list.add(2)
        with self.assertRaises(IndexError) as context:
            self.list.remove_index(2)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_init_method_takes_integers_only(self):
        lst = IntegerList(1, 2, 3, "4")
        self.assertEqual(lst.get_data(), [1, 2, 3])

    def test_get_method_return_correct_element(self):
        self.list.add(1)
        element = self.list.get(0)
        self.assertEqual(element, 1)

    def test_get_method_incorrect_index_raise_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.list.get(0)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_method_incorrect_index_raise_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.list.insert(0, 1)
        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_method_type_element_raise_value_error(self):
        self.list.add(1)
        with self.assertRaises(ValueError) as context:
            self.list.insert(0, "1")
        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_insert_correct_index_and_element(self):
        self.list.add(1)
        self.list.insert(0, 2)
        self.assertEqual(self.list.get_data(), [2, 1])

    def test_get_biggest_to_return_biggest_number(self):
        self.list.add(1)
        self.list.add(2)
        self.assertEqual(self.list.get_biggest(), 2)

    def test_get_index(self):
        self.list.add(11)
        self.assertEqual(self.list.get_index(11), 0)


if __name__ == "__main__":
    unittest.main()
