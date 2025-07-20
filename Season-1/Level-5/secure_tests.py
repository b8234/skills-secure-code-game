# tests.py

import unittest
import secure_code as c  # assumes you've saved the secure version as secure_code.py

class TestCryptoSecure(unittest.TestCase):

    def setUp(self):
        self.generator = c.RandomGenerator()
        self.hasher = c.PasswordHasher()

    def test_token_generation_is_secure_and_unique(self):
        token1 = self.generator.generate_token()
        token2 = self.generator.generate_token()
        self.assertIsInstance(token1, str)
        self.assertIsInstance(token2, str)
        self.assertNotEqual(token1, token2)
        self.assertGreaterEqual(len(token1), 32)

    def test_password_hash_and_verify_success(self):
        password = "Secur3P@ssw0rd!"
        hashed = self.hasher.password_hash(password)
        result = self.hasher.password_verification(password, hashed)
        self.assertTrue(result)

    def test_password_hash_and_verify_failure(self):
        password = "correct_horse_battery_staple"
        wrong_password = "Tr0ub4dor&3"
        hashed = self.hasher.password_hash(password)
        result = self.hasher.password_verification(wrong_password, hashed)
        self.assertFalse(result)

    def test_password_hash_returns_string(self):
        password = "testpassword"
        hashed = self.hasher.password_hash(password)
        self.assertIsInstance(hashed, str)

    def test_password_verification_type_check(self):
        # invalid types should fail gracefully
        self.assertFalse(self.hasher.password_verification(None, None))
        self.assertFalse(self.hasher.password_verification("password", None))
        self.assertFalse(self.hasher.password_verification(None, "hash"))

if __name__ == '__main__':
    unittest.main()
