from unittest import TestCase, main
from project.bookstore import Bookstore


class Tests(TestCase):
    def setUp(self):
        self.book_store = Bookstore(10)

    def test_correct_init(self):
        self.assertEqual(10, self.book_store.books_limit)
        self.assertEqual(0, self.book_store._Bookstore__total_sold_books)
        self.assertEqual({}, self.book_store.availability_in_store_by_book_titles)

    def test_invalid_initialize_book_limit(self):
        expected = f'Books limit of 0 is not valid'
        with self.assertRaises(ValueError) as ve:
            Bookstore(0)
        self.assertEqual(expected, str(ve.exception))

    def test_count_how_many_books_we_got_available(self):
        self.book_store.availability_in_store_by_book_titles = {"The Big Bang Theory": 2, "What is Space": 9}
        self.assertEqual(11, len(self.book_store))

    def test_receiving_to_many_books(self):
        expected = f'Books limit is reached. Cannot receive more books!'
        with self.assertRaises(Exception) as ex:
            self.book_store.receive_book('Time and Space', 75)
        self.assertEqual(expected, str(ex.exception))

    def test_receiving_new_book(self):
        result = self.book_store.receive_book('What is why', 2)
        self.assertEqual(2, len(self.book_store))
        self.assertEqual('2 copies of What is why are available in the bookstore.', result)

    def test_receiving_stock(self):
        self.book_store.availability_in_store_by_book_titles = {"What is why": 2, "Why is What": 2}
        result = self.book_store.receive_book('What is why', 2)
        self.assertEqual(2, len(self.book_store.availability_in_store_by_book_titles))
        self.assertEqual('4 copies of What is why are available in the bookstore.', result)

    def test_selling_a_book_not_in_store(self):
        expected = "Book Time and Space doesn't exist!"
        with self.assertRaises(Exception) as ex:
            self.book_store.sell_book('Time and Space', 75)
        self.assertEqual(expected, str(ex.exception))

    def test_selling_more_then_we_got_in_store(self):
        self.book_store.availability_in_store_by_book_titles = {"Time and Space": 2, "Why is What": 2}
        expected = "Time and Space has not enough copies to sell. Left: 2"
        with self.assertRaises(Exception) as ex:
            self.book_store.sell_book('Time and Space', 75)
        self.assertEqual(expected, str(ex.exception))

    def test_selling_out_a_book(self):
        self.book_store.availability_in_store_by_book_titles = {"Time and Space": 2, "Why is What": 2}
        result = self.book_store.sell_book('Time and Space', 2)
        self.assertEqual('Sold 2 copies of Time and Space', result)
        self.assertEqual(2, self.book_store._Bookstore__total_sold_books)
        self.assertEqual({"Time and Space": 0, "Why is What": 2}, self.book_store.availability_in_store_by_book_titles)

    def test_print_in_stock(self):
        self.book_store.availability_in_store_by_book_titles = {"Time and Space": 2}
        expected = f'Total sold books: 0\nCurrent availability: 2\n - Time and Space: 2 copies'
        self.assertEqual(expected, str(self.book_store))

