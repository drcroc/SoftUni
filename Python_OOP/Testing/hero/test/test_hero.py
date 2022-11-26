from project.hero import Hero
from unittest import TestCase, main


class Tests(TestCase):
    def setUp(self):
        self.hero = Hero('hero', 5, 10, 2)
        self.enemy_draw = Hero('enemy_one', 5, 10, 2)
        self.enemy_win = Hero('enemy_two', 10, 15, 8)
        self.enemy_lose = Hero('enemy_two', 1, 3, 1)

    def test_battle_yourself(self):
        expected = 'You cannot fight yourself'

        with self.assertRaises(Exception) as exception:
            self.hero.battle(self.hero)

        self.assertEqual(expected, str(exception.exception))

    def test_battle_with_zero_hp_hero(self):
        self.hero.health = 0
        expected = 'Your health is lower than or equal to 0. You need to rest'

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_draw)

        self.assertEqual(expected, str(ve.exception))

    def test_battle_with_zero_hp_enemy(self):
        self.enemy_draw.health = 0
        expected = f'You cannot fight {self.enemy_draw.username}. He needs to rest'

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy_draw)

        self.assertEqual(expected, str(ve.exception))

    def test_draw_battle(self):
        expected = f'Draw'
        actual = self.hero.battle(self.enemy_draw)

        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy_draw.health)
        self.assertEqual(expected, actual)

    def test_battle_hero_wins(self):
        expected = f'You win'
        actual = self.hero.battle(self.enemy_lose)

        self.assertEqual(6, self.hero.level)
        self.assertEqual(14, self.hero.health)
        self.assertEqual(7, self.hero.damage)
        self.assertEqual(expected, actual)

    def test_battle_hero_losses(self):
        expected = f'You lose'
        actual = self.hero.battle(self.enemy_win)

        self.assertEqual(11, self.enemy_win.level)
        self.assertEqual(10, self.enemy_win.health)
        self.assertEqual(13, self.enemy_win.damage)
        self.assertEqual(expected, actual)

    def test_hero_stats(self):
        expected = f"Hero hero: 5 lvl\n" \
                    f"Health: 10\n" \
                    f"Damage: 2\n"
        actual = self.hero.__str__()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()

