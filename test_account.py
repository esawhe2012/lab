# Author: Isai Rangel
# Date: 04-21-2023
import unittest
from account import *


class Test(unittest.TestCase):

    def setup_method(self):
        self.a1 = Account('John')
        self.a2 = Account('Patty')

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == 'John'
        assert self.a1.get_balance() == 0

    def test_deposit(self):
        self.assertEqual(self.a1.deposit(100), True)
        self.assertEqual(self.a1.deposit(-100), False)
        self.assertEqual(self.a1.deposit(0), False)

    def test_withdraw(self):
        self.a1.deposit(100)  # Set to 100 to test
        self.assertEqual(self.a1.withdraw(150), False)
        self.assertEqual(self.a1.withdraw(0), False)
        self.assertEqual(self.a1.withdraw(50), True)

    def test_get_balance(self):
        assert self.a2.get_balance() == 0

    def test_get_name(self):
        assert self.a1.get_name() == 'John'
