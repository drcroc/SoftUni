from project.toy_store import ToyStore
from unittest import TestCase, main


class Tests(TestCase):      # points 80 / 100
    def setUp(self):
        self.toy_store = ToyStore()

    def test_init_shelf(self):
        self.assertEqual({'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.toy_store.toy_shelf)

    def test_all_shelves_are_full(self):
        self.toy_store.toy_shelf = {'A': 'Elf',
                                    'B': "Moose",
                                    'C': 'Bear',
                                    'D': 'Dear',
                                    'E': "Rabbit",
                                    'F': 'Horse',
                                    'G': 'Dog'}

        self.assertEqual({
            'A': 'Elf',
            'B': "Moose",
            'C': 'Bear',
            'D': 'Dear',
            'E': "Rabbit",
            'F': 'Horse',
            'G': 'Dog'
        }, self.toy_store.toy_shelf)

    def test_add_toy_to_not_existing_shelf(self):
        expected = f"Shelf doesn't exist!"

        with self.assertRaises(Exception) as ve:
            self.toy_store.add_toy('I', 'Elf')
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual({'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.toy_store.toy_shelf)

    def test_add_second_toy_to_the_same_shelf(self):
        expected = f"Toy is already in shelf!"
        self.toy_store.add_toy('B', 'Elf')

        with self.assertRaises(Exception) as ve:
            self.toy_store.add_toy('B', 'Elf')

        self.assertEqual('Elf', self.toy_store.toy_shelf['B'])
        self.assertEqual(expected, str(ve.exception))
        self.assertEqual({'A': None, 'B': 'Elf', 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.toy_store.toy_shelf)

    def test_add_second_toy_to_already_taken_shelf(self):
        expected = f"Shelf is already taken!"
        self.toy_store.add_toy('B', 'Dear')

        with self.assertRaises(Exception) as ve:
            self.toy_store.add_toy('B', 'Elf')

        self.assertEqual(expected, str(ve.exception))
        self.assertEqual('Dear', self.toy_store.toy_shelf['B'])
        self.assertEqual({'A': None, 'B': 'Dear', 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.toy_store.toy_shelf)

    def test_add_toy_to_empty_shelf(self):
        self.assertEqual({'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.toy_store.toy_shelf)

        self.toy_store.add_toy('B', 'Elf')
        self.assertEqual({'A': None, 'B': 'Elf', 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.toy_store.toy_shelf)

    def test_remove_toy_from_not_existing_shelf(self):
        expected = f"Shelf doesn't exist!"

        with self.assertRaises(Exception) as ve:
            self.toy_store.remove_toy('I', 'Elf')

        self.assertEqual(expected, str(ve.exception))
        self.assertEqual({'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.toy_store.toy_shelf)

    def test_remove_toy_from_different_shelf(self):
        expected = f"Toy in that shelf doesn't exists!"
        self.toy_store.add_toy('C', 'Dear')

        with self.assertRaises(Exception) as ve:
            self.toy_store.remove_toy('C', 'Elf')

        self.assertEqual(expected, str(ve.exception))
        self.assertEqual({'A': None, 'B': None, 'C': 'Dear', 'D': None, 'E': None, 'F': None, 'G': None},
                         self.toy_store.toy_shelf)

    def test_remove_toy_successfully(self):
        self.toy_store.add_toy('B', 'Elf')
        self.assertEqual({'A': None, 'B': 'Elf', 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.toy_store.toy_shelf)

        self.toy_store.remove_toy('B', 'Elf')
        self.assertEqual({'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.toy_store.toy_shelf)

    def test_items_count(self):
        self.toy_store.add_toy('B', 'Elf')
        self.assertEqual(7, len(self.toy_store.toy_shelf))


if __name__ == '__main__':
    main()

    # points 80 / 100
