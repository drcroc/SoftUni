from project.vehicle import Vehicle
from unittest import TestCase, main


class Test(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(10, 90)

    def test_drive_with_full_fuel_in_tank(self):
        self.vehicle.drive(5)
        actual = self.vehicle.fuel
        expected = 3.75
        self.assertEqual(expected, actual)

    def test_drive_with_zero_fuel_in_tank(self):

        expected = 'Not enough fuel'

        with self.assertRaises(Exception) as context:
            self.vehicle.drive(20)

        self.assertTrue(expected in str(context.exception))

    def test_refuel_with_over_the_tank_limit(self):

        expected = 'Too much fuel'
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(5)

        self.assertTrue(expected in str(context.exception))

    def test_refuel_with_zero_fuel_in_tank(self):
        self.vehicle.drive(5)
        self.vehicle.refuel(2)
        actual = self.vehicle.fuel
        expected = 5.75
        self.assertEqual(expected, actual)

    def test_get_class_str(self):
        actual = self.vehicle.__str__()
        expected = 'The vehicle has 90 horse power with 10 fuel left and 1.25 fuel consumption'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    main()
