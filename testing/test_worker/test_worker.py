from worker import Worker
import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker("Jordan", 100, 100)

    def test_worker_init_correct_name_salary_energy(self):
        self.assertEqual(self.worker.name, "Jordan")
        self.assertEqual(self.worker.salary, 100)
        self.assertEqual(self.worker.energy, 100)

    def test_rest_method_and_increase_energy_by_one(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 101)

    def test_raised_an_error_with_given_zero_energy_to_work_method(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_raised_an_error_with_given_negative_energy_to_work_method(self):
        self.worker.energy = -1
        with self.assertRaises(Exception):
            self.worker.work()

    def test_correct_money_increase_after_work_method(self):
        self.worker.work()
        self.assertEqual(self.worker.money, 100)

    def test_correct_energy_decrease_by_one_after_work_method(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 99)

    def test_get_info_return_correct_string_representation(self):
        info = self.worker.get_info()
        result = f"{self.worker.name} has saved {self.worker.money} money."
        self.assertEqual(info, result)


if __name__ == "__main__":
    unittest.main()
