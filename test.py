import unittest
from manager import Manager

class TestManager(unittest.TestCase):
    
    def test_create_password(self):
        manager = Manager()
        password = manager.create_password(10)
        self.assertEqual(len(password), 10)
        password = manager.create_password(0)
        self.assertEqual(password, "")

    def test_contains_prohibited(self):
        manager = Manager()
        self.assertTrue(manager.contains_prohibited("pass word"))
        self.assertFalse(manager.contains_prohibited("password"))

    def test_clear_passwords(self):
        manager = Manager()
        manager.set_password("Facebook", "password")
        manager.clear_passwords()
        self.assertEqual(manager.get_credentials(), {})

    def test_list_websites(self):
        manager = Manager()
        manager.clear_passwords()
        self.assertEqual(manager.list_websites(), [])
        manager.set_password("Facebook", "password")
        self.assertEqual(manager.list_websites(), ["Facebook"])

    def test_get_password(self):
        manager = Manager()
        manager.clear_passwords()
        self.assertFalse(manager.get_password("Facebook"))
        manager.set_password("Facebook", "password")
        self.assertEqual(manager.get_password("Facebook"), "password")

    def test_change_password(self):
        manager = Manager()
        manager.clear_passwords()
        manager.set_password("Facebook", "password")
        manager.change_password("Facebook", "password", "new_password")
        self.assertEqual(manager.get_password("Facebook"), "new_password")
        manager.change_password("Facebook", "password", "new_password")
        self.assertFalse(manager.change_password("Facebook", "password", "new_password"))

if __name__ == "__main__":
    unittest.main()