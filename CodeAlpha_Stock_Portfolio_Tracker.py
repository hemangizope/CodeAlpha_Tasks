def main():
    # 1. Hardcoded dictionary of stock prices
    stock_prices = {
        "AAPL": 175.50,
        "GOOGL": 140.25,
        "TSLA": 210.10,
        "AMZN": 170.80,
        "MSFT": 405.30
    }

    print("--- Simple Stock Portfolio Tracker ---")
    print(f"Available stocks: {', '.join(stock_prices.keys())}\n")

    # 2. User input for stock name and quantity
    ticker = input("Enter the stock ticker (e.g., AAPL): ").upper()
    
    if ticker not in stock_prices:
        print(f"Sorry, {ticker} is not in our database.")
        return

    try:
        quantity = int(input(f"How many shares of {ticker} do you own? "))
    except ValueError:
        print("Invalid input. Please enter a whole number for quantity.")
        return

    # 3. Basic arithmetic: Calculate total value
    price = stock_prices[ticker]
    total_value = price * quantity

    # Display result
    result_message = f"Portfolio Update: {quantity} shares of {ticker} at ${price} each. Total Value: ${total_value:,.2f}"
    print(f"\n{result_message}")

    # 4. Save result to a .txt file
    save_choice = input("\nWould you like to save this result to a file? (y/n): ").lower()
    if save_choice == 'y':
        with open("portfolio_summary.txt", "a") as file:
            file.write(result_message + "\n")
        print("Summary saved to portfolio_summary.txt")

if __name__ == "__main__":
    main()