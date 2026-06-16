"""Stock Portfolio Tracker"""

import csv
import os
from datetime import date

# Hardcoded stock prices dictionary
STOCK_PRICES = {
    "AAPL": 189.50,
    "TSLA": 248.75,
    "GOOGL": 175.20,
    "AMZN": 198.30,
    "MSFT": 415.60,
    "META": 520.10,
    "NFLX": 640.80,
    "NVDA": 130.45,
}


def display_available_stocks():
    """Display all available stocks with their current prices."""
    print("\n" + "=" * 45)
    print("       AVAILABLE STOCKS & PRICES")
    print("=" * 45)
    print(f"{'Symbol':<12} {'Price (USD/INR)':>15}")
    print("-" * 45)
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<10} ${price:>14,.2f}")
    print("=" * 45)


def get_stock_input():
    """Get stock name and quantity from user."""
    portfolio = {}

    print("\n📈 Enter your stock holdings.")
    print("   Type 'done' when finished.\n")

    while True:
        symbol = input("  Stock symbol (e.g. AAPL): ").strip().upper()

        if symbol.lower() == "done":
            if not portfolio:
                print("  ⚠ No stocks added yet. Please add at least one.")
                continue
            break

        if symbol not in STOCK_PRICES:
            print(f"  ❌ '{symbol}' not found. Choose from available stocks above.\n")
            continue

        try:
            qty_input = input(f"  Quantity of {symbol}: ").strip()
            quantity = int(qty_input)
            if quantity <= 0:
                print("  ⚠ Quantity must be a positive number.\n")
                continue
        except ValueError:
            print("  ⚠ Please enter a valid whole number.\n")
            continue

        if symbol in portfolio:
            portfolio[symbol] += quantity
            print(f"  ✅ Updated {symbol}: total {portfolio[symbol]} shares.\n")
        else:
            portfolio[symbol] = quantity
            print(f"  ✅ Added {symbol} x{quantity}.\n")

    return portfolio


def calculate_portfolio(portfolio):
    """Calculate total investment value for each stock."""
    results = []
    grand_total = 0.0

    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * quantity
        grand_total += value
        results.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "value": value,
        })

    return results, grand_total


def display_portfolio_summary(results, grand_total):
    """Display the portfolio summary in a formatted table."""
    print("\n" + "=" * 60)
    print("             📊 PORTFOLIO SUMMARY")
    print("=" * 60)
    print(f"  {'Stock':<8} {'Qty':>6} {'Price':>12} {'Total Value':>14}")
    print("-" * 60)

    for row in results:
        print(f"  {row['symbol']:<8} {row['quantity']:>6} "
              f"${row['price']:>11,.2f} ${row['value']:>13,.2f}")

    print("-" * 60)
    print(f"  {'GRAND TOTAL':>28} ${grand_total:>13,.2f}")
    print("=" * 60)
    print(f"\n  📅 Date: {date.today()}")


def save_to_file(results, grand_total):
    """Save portfolio to both .txt and .csv files."""
    today = str(date.today())

    # Save as TXT
    txt_filename = f"portfolio_{today}.txt"
    with open(txt_filename, "w") as f:
        f.write("STOCK PORTFOLIO TRACKER")
        f.write(f"Date: {today}\n")
        f.write("=" * 55 + "\n")
        f.write(f"{'Stock':<10} {'Qty':>6} {'Price':>12} {'Total Value':>14}\n")
        f.write("-" * 55 + "\n")
        for row in results:
            f.write(f"{row['symbol']:<10} {row['quantity']:>6} "
                    f"${row['price']:>11,.2f} ${row['value']:>13,.2f}\n")
        f.write("-" * 55 + "\n")
        f.write(f"{'GRAND TOTAL':>30} ${grand_total:>13,.2f}\n")

    # Save as CSV
    csv_filename = f"portfolio_{today}.csv"
    with open(csv_filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["symbol", "quantity", "price", "value"])
        writer.writeheader()
        writer.writerows(results)
        writer.writerow({"symbol": "TOTAL", "quantity": "", "price": "", "value": grand_total})

    print(f"\n  💾 Saved: {txt_filename}")
    print(f"  💾 Saved: {csv_filename}")


def main():
    print("\n" + "=" * 45)
    print("       STOCK PORTFOLIO TRACKER")
    print("=" * 45)

    display_available_stocks()

    portfolio = get_stock_input()
    results, grand_total = calculate_portfolio(portfolio)
    display_portfolio_summary(results, grand_total)

    save_choice = input("\n  💾 Save results to file? (y/n): ").strip().lower()
    if save_choice == "y":
        save_to_file(results, grand_total)

    print("\n  ✅ Thank you for using Stock Portfolio Tracker!")
    print("=" * 45 + "\n")


if __name__ == "__main__":
    main()
