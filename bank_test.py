import unittest
import bank


class TestBank(unittest.TestCase):
    def setUp(self):
        self.account = bank.bank("George", 1000)

    def test_deposit(self):
        self.assertTrue(self.account.deposit(500))
        self.assertEqual(self.account.get_balance(), 1500)
        self.assertFalse(self.account.deposit(-100))

    def test_withdraw(self):
        self.assertTrue(self.account.withdraw(200))
        self.assertEqual(self.account.get_balance(), 800)
        self.assertFalse(self.account.withdraw(900))  # Overdraft
        self.assertFalse(self.account.withdraw(-100))  # Invalid amount

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_get_name(self):
        self.assertEqual(self.account.get_name(), "George")
