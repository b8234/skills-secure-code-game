# secure_test_runner.py

import os
from secure_code import SecureStockDB

def run_mode(mode: str):
    print(f"\n=== Running in LOG_MODE: {mode.upper()} ===")
    try:
        db = SecureStockDB(log_mode=mode)

        info = db.get_stock_info("MSFT")
        print("\n[Stock Info Result]")
        print(info)

        price = db.get_stock_price("MSFT")
        print("\n[Stock Price Result]")
        print(price)

        updated = db.update_stock_price("MSFT", 320.0)
        print("\n[Update Price Result]")
        print(updated)

        print(f"\n✅ PASS: {mode} mode executed without error.")
    except Exception as e:
        print(f"\n❌ FAIL: Error in {mode} mode - {e}")


if __name__ == "__main__":
    print(">>> SecureStockDB Test Harness <<<")
    
    # Test secure mode
    run_mode("secure")

    # Test compatible mode (for legacy test harness expectations)
    run_mode("compatible")
