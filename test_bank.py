import unittest
import bank


class TestBank(unittest.TestCase):
    def test_deposit(self):
        account1 = bank.bank("George", 1000)
        self.assertTrue(account1.deposit(500))
        self.assertEqual(account1.get_balance(), 1500)
        self.assertFalse(account1.deposit(-100))
        self.assertFalse(account1.deposit("a"))
        self.assertEqual(account1.get_balance(), 1500)

    def test_withdraw(self):
        account2 = bank.bank("George", 1000)
        self.assertTrue(account2.withdraw(200))
        self.assertEqual(account2.get_balance(), 800)
        self.assertFalse(account2.withdraw(900))
        self.assertFalse(account2.withdraw(-100))
        self.assertFalse(account2.withdraw("b"))
        self.assertEqual(account2.get_balance(), 800)

    def test_get_balance(self):
        account3 = bank.bank("George", 1000)
        self.assertEqual(account3.get_balance(), 1000)

    def test_get_name(self):
        account4 = bank.bank("George", 1000)
        self.assertEqual(account4.get_name(), "George")
