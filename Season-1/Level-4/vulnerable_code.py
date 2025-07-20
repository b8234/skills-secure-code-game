import sqlite3
import os
from flask import Flask, request

# Flask app (not used in tests, safe to ignore)
app = Flask(__name__)

@app.route("/")
def source():
    DB_CRUD_ops().get_stock_info(request.args["input"])
    DB_CRUD_ops().get_stock_price(request.args["input"])
    DB_CRUD_ops().update_stock_price(request.args["input"])

class Connect(object):
    def create_connection(self, path):
        connection = None
        try:
            connection = sqlite3.connect(path)
        except sqlite3.Error as e:
            print(f"ERROR: {e}")
        return connection

class Create(object):
    def __init__(self):
        con = Connect()
        try:
            path = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(path, 'level-4.db')
            db_con = con.create_connection(db_path)
            cur = db_con.cursor()
            table_fetch = cur.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='stocks';"
            ).fetchall()
            if table_fetch == []:
                cur.execute("CREATE TABLE stocks (date text, symbol text, price real)")
                cur.execute("INSERT INTO stocks VALUES (?, ?, ?)", ('2022-01-06', 'MSFT', 300.00))
                db_con.commit()
        except sqlite3.Error as e:
            print(f"ERROR: {e}")
        finally:
            db_con.close()

class DB_CRUD_ops(object):
    def get_stock_info(self, stock_symbol):
        db = Create()
        con = Connect()
        try:
            path = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(path, 'level-4.db')
            db_con = con.create_connection(db_path)
            cur = db_con.cursor()
            res = "[METHOD EXECUTED] get_stock_info\n"
            res += "[QUERY] SELECT * FROM stocks WHERE symbol = '{}'\n".format(stock_symbol)

            restricted_chars = ";%&^!#-"
            has_restricted_char = any([char in stock_symbol for char in restricted_chars])
            correct_number_of_single_quotes = stock_symbol.count("'") == 0

            if has_restricted_char or not correct_number_of_single_quotes:
                res += "CONFIRM THAT THE ABOVE QUERY IS NOT MALICIOUS TO EXECUTE"
            else:
                cur.execute("SELECT * FROM stocks WHERE symbol = ?", (stock_symbol,))
                query_outcome = cur.fetchall()
                for result in query_outcome:
                    res += "[RESULT] " + str(result)
            return res
        except sqlite3.Error as e:
            print(f"ERROR: {e}")
        finally:
            db_con.close()

    def get_stock_price(self, stock_symbol):
        db = Create()
        con = Connect()
        try:
            path = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(path, 'level-4.db')
            db_con = con.create_connection(db_path)
            cur = db_con.cursor()
            res = "[METHOD EXECUTED] get_stock_price\n"
            res += "[QUERY] SELECT price FROM stocks WHERE symbol = '{}'\n".format(stock_symbol)

            restricted_chars = ";%&^!#-"
            has_restricted_char = any([char in stock_symbol for char in restricted_chars])
            correct_number_of_single_quotes = stock_symbol.count("'") == 0

            if has_restricted_char or not correct_number_of_single_quotes:
                res += "CONFIRM THAT THE ABOVE QUERY IS NOT MALICIOUS TO EXECUTE"
            else:
                cur.execute("SELECT price FROM stocks WHERE symbol = ?", (stock_symbol,))
                query_outcome = cur.fetchall()
                for result in query_outcome:
                    res += "[RESULT] " + str(result) + "\n"
            return res
        except sqlite3.Error as e:
            print(f"ERROR: {e}")
        finally:
            db_con.close()

    def update_stock_price(self, stock_symbol, price):
        db = Create()
        con = Connect()
        try:
            path = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(path, 'level-4.db')
            db_con = con.create_connection(db_path)
            cur = db_con.cursor()
            if not isinstance(price, float):
                raise Exception("ERROR: stock price provided is not a float")
            res = "[METHOD EXECUTED] update_stock_price\n"
            res += "[QUERY] UPDATE stocks SET price = '{}' WHERE symbol = '{}'\n".format(int(price), stock_symbol)
            cur.execute("UPDATE stocks SET price = ? WHERE symbol = ?", (price, stock_symbol))
            db_con.commit()
            return res
        except sqlite3.Error as e:
            print(f"ERROR: {e}")
        finally:
            db_con.close()
