# secure_code.py

import sqlite3
import os
from typing import Optional


class DatabaseConnection:
    """Context manager for SQLite database connection."""
    def __init__(self, db_filename: str = 'level-4.db'):
        self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), db_filename)

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()


class SecureStockDB:
    """
    Professional-grade database interface for stock operations.
    Designed for secure, testable, production use.
    """
    def __init__(self, log_mode: str = "secure"):
        assert log_mode in {"secure", "compatible"}, "log_mode must be 'secure' or 'compatible'"
        self.log_mode = log_mode
        self._initialize_db()

    def _initialize_db(self):
        with DatabaseConnection() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS stocks (
                    date TEXT,
                    symbol TEXT PRIMARY KEY,
                    price REAL
                )
            """)
            cur.execute("SELECT COUNT(*) FROM stocks WHERE symbol = ?", ('MSFT',))
            if cur.fetchone()[0] == 0:
                cur.execute("INSERT INTO stocks VALUES (?, ?, ?)", ('2022-01-06', 'MSFT', 300.0))

    def _is_safe_symbol(self, symbol: str) -> bool:
        """Validate stock symbol: uppercase, alphanumeric, ≤ 5 characters."""
        return symbol.isalnum() and symbol.isupper() and len(symbol) <= 5

    def get_stock_info(self, symbol: str) -> str:
        log = "[METHOD EXECUTED] get_stock_info\n"
        log += self._log_query("SELECT * FROM stocks WHERE symbol = ?", symbol)

        if not self._is_safe_symbol(symbol):
            log += "CONFIRM THAT THE ABOVE QUERY IS NOT MALICIOUS TO EXECUTE"
            return log

        with DatabaseConnection() as cur:
            cur.execute("SELECT * FROM stocks WHERE symbol = ?", (symbol,))
            result = cur.fetchone()
            log += "[RESULT] " + str(result) if result else "[RESULT] No entry found."
            return log

    def get_stock_price(self, symbol: str) -> str:
        log = "[METHOD EXECUTED] get_stock_price\n"
        log += self._log_query("SELECT price FROM stocks WHERE symbol = ?", symbol)

        if not self._is_safe_symbol(symbol):
            log += "CONFIRM THAT THE ABOVE QUERY IS NOT MALICIOUS TO EXECUTE"
            return log

        with DatabaseConnection() as cur:
            cur.execute("SELECT price FROM stocks WHERE symbol = ?", (symbol,))
            result = cur.fetchone()
            log += "[RESULT] " + str(result) + "\n" if result else "[RESULT] No price found.\n"
            return log

    def update_stock_price(self, symbol: str, price: float) -> str:
        log = "[METHOD EXECUTED] update_stock_price\n"
        log += self._log_query("UPDATE stocks SET price = ? WHERE symbol = ?", symbol, price)

        if not self._is_safe_symbol(symbol):
            raise ValueError("Unsafe stock symbol input.")
        if not isinstance(price, float):
            raise ValueError("Stock price must be a float.")

        with DatabaseConnection() as cur:
            cur.execute("UPDATE stocks SET price = ? WHERE symbol = ?", (price, symbol))
            return log

    def _log_query(self, query: str, symbol: str, price: Optional[float] = None) -> str:
        """
        Internal utility to return log output for a query depending on log_mode.
        """
        if self.log_mode == "secure":
            return f"[QUERY] {query}\n"
        elif "price" in query and price is not None:
            return f"[QUERY] UPDATE stocks SET price = '{int(price)}' WHERE symbol = '{symbol}'\n"
        else:
            interpolated = query.replace("?", f"'{symbol}'")
            return f"[QUERY] {interpolated}\n"
