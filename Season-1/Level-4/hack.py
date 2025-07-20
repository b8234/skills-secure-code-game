'''
Please note:

The first file that you should run in this level is tests.py for database creation, with all tests passing.
Remember that running the hack.py will change the state of the database, causing some tests inside tests.py
to fail.

If you like to return to the initial state of the database, please delete the database (level-4.db) and run 
the tests.py again to recreate it.
'''

import unittest
import secure_code as c



# code.py has 5 methods namely:
# (1) get_stock_info
# (2) get_stock_price
# (3) update_stock_price
# (4) exec_multi_query
# (5) exec_user_script

# All methods were vulnerable.
# We believe that methods (4) and (5) shouldn't exist at all in the code.
# Have a look at solution.py for the reasoning.

class TestDatabase(unittest.TestCase):

    # This test simulates an attempted SQL injection using a semicolon
    # to chain another query to the original one.
    def test_1(self):
        #op = c.DB_CRUD_ops()
        op = c.SecureStockDB(log_mode='secure')

        # Expected safe usage
        developer_expectation = op.get_stock_price('MSFT')
        developer_output_expectation = "[METHOD EXECUTED] get_stock_price\n[QUERY] SELECT price FROM stocks WHERE symbol = 'MSFT'\n[RESULT] (300.0,)\n"
        self.assertEqual(developer_output_expectation, developer_expectation)

        # Malicious input to test injection defense
        what_hacker_passes = op.get_stock_price("MSFT'; UPDATE stocks SET price = '525' WHERE symbol = 'MSFT'--")
        expected_output = "[METHOD EXECUTED] get_stock_price\n[QUERY] SELECT price FROM stocks WHERE symbol = 'MSFT'; UPDATE stocks SET price = '525' WHERE symbol = 'MSFT'--'\nCONFIRM THAT THE ABOVE QUERY IS NOT MALICIOUS TO EXECUTE"
        self.assertEqual(expected_output, what_hacker_passes)
        
        # but the hacker passes is this:
        #what_hacker_passes = op.get_stock_price("MSFT'; UPDATE stocks SET price = '525' WHERE symbol = 'MSFT'--")
        #hacker_output = "[METHOD EXECUTED] get_stock_price\n[QUERY] SELECT price FROM stocks WHERE symbol = 'MSFT'; UPDATE stocks SET price = '525' WHERE symbol = 'MSFT'--'\n[SCRIPT EXECUTION]\n"

        #self.assertEqual(developer_output_expectation, what_hacker_passes)

# Further exploit input could be:
# op.get_stock_price("MSFT'; DROP TABLE stocks--")

if __name__ == '__main__':
    unittest.main()
