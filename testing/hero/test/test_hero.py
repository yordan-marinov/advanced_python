import unittest

from project.hero import Hero


class HeroTests(unittest.TestCase):
    username = "Jordan"
    level = 1
    health = 100.0
    damage = 10.0

    def setUp(self):
        self.h = Hero(self.username, self.level, self.health, self.damage)
        self.eh = Hero(self.username, self.level, self.health, self.damage)

    def test_h_correct_init(self):
        self.assertEqual(self.username, self.h.username)
        self.assertEqual(self.level, self.h.level)
        self.assertEqual(self.health, self.h.health)
        self.assertEqual(self.damage, self.h.damage)

    def test_eh_correct_init(self):
        self.assertEqual(self.username, self.eh.username)
        self.assertEqual(self.level, self.eh.level)
        self.assertEqual(self.health, self.eh.health)
        self.assertEqual(self.damage, self.eh.damage)

    def test_battle_when_username_and_enemy_username_is_same_shoud_raise_exception(
        self,
    ):
        with self.assertRaises(Exception) as contex:
            self.h.battle(self.eh)
        self.assertEqual("You cannot fight yourself", str(contex.exception))

    def test_battle_when_self_self_health_is_equal_to_zero_should_raise_value_error(
        self,
    ):
        self.eh.username = "Martin"
        self.h.health = 0
        with self.assertRaises(ValueError) as contex:
            self.h.battle(self.eh)

        self.assertEqual(
            f"Your health is lower than or equal to 0. You need to rest",
            str(contex.exception),
        )

    def test_battle_when_self_self_health_is_negative_shoud_raise_value_error(self):
        self.eh.username = "Martin"
        self.h.health = -1
        with self.assertRaises(ValueError) as contex:
            self.h.battle(self.eh)

        self.assertEqual(
            f"Your health is lower than or equal to 0. You need to rest",
            str(contex.exception),
        )

    def test_battle_when_self_enemy_health_is_equal_to_zero_should_raise_value_error(
        self,
    ):
        self.eh.username = "Martin"
        self.eh.health = 0
        with self.assertRaises(ValueError) as contex:
            self.h.battle(self.eh)

        self.assertEqual(
            f"You cannot fight {self.eh.username}. He needs to rest",
            str(contex.exception),
        )

    def test_battle_when_self_enemy_health_is_negative_shoud_raise_value_error(self):
        self.eh.username = "Martin"
        self.eh.health = -1
        with self.assertRaises(ValueError) as contex:
            self.h.battle(self.eh)

        self.assertEqual(
            f"You cannot fight {self.eh.username}. He needs to rest",
            str(contex.exception),
        )

    def test_battle_if_self_and_enemy_health_below_and_equal_zero_retrun_draw(self):
        self.eh.username = "Martin"
        self.h.damage = 100
        self.eh.damage = 100
        self.assertEqual("Draw", self.h.battle(self.eh))

    def test_battle_if_enemy_health_below_and_equal_zero_retrun_you_win(self):
        self.eh.username = "Martin"
        self.h.damage = 100
        self.eh.damage = 0
        self.assertEqual("You win", self.h.battle(self.eh))
        self.assertEqual(2, self.h.level)
        self.assertEqual(105.0, self.h.health)
        self.assertEqual(105, self.h.damage)

    def test_battle_if_self_health_below_and_equal_zero_retrun_you_win(self):
        self.eh.username = "Martin"
        self.h.damage = 0
        self.eh.damage = 100
        self.assertEqual("You lose", self.h.battle(self.eh))
        self.assertEqual(2, self.eh.level)
        self.assertEqual(105.0, self.eh.health)
        self.assertEqual(105, self.eh.damage)

    def test__str__representation(self):
        expected = (
            f"Hero {self.h.username}: {self.h.level} lvl\n"
            f"Health: {self.h.health}\n"
            f"Damage: {self.h.damage}\n"
        )
        self.assertEqual(expected, str(self.h))

if __name__ == "__main__":
    unittest.main()