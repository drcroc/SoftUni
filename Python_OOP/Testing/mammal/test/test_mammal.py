from project.mammal import Mammal
from unittest import TestCase, main


class Tests(TestCase):

    def setUp(self):
        self.cat = Mammal('cat', 'mammals', 'Meow')

    def test_check_anima_sound(self):
        actual = self.cat.make_sound()
        expected = 'cat makes Meow'
        self.assertEqual(actual, expected)

    def test_is_the_animal_in_the_animal_kingdom(self):
        actual = self.cat.get_kingdom()
        expected = 'animals'
        self.assertEqual(actual, expected)

    def test_check_info_if_it_is_the_same(self):
        actual = self.cat.info()
        expected = 'cat is of type mammals'
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    main()
