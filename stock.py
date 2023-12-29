import yfinance as yf

def calculate_PEG(ticker):
    stock = yf.Ticker(ticker)
    pe_ratio = stock.info.get('trailingPE')
    peg_ratio = None

    if pe_ratio is not None:
        peg_ratio = pe_ratio / stock.info.get('pegRatio', None)

    return peg_ratio

def calculate_PS_ratio(ticker):
    stock = yf.Ticker(ticker)
    price = stock.info.get('regularMarketPrice')
    revenue_per_share = stock.info.get('revenuePerShare')
    ps_ratio = None

    if price is not None and revenue_per_share is not None and revenue_per_share != 0:
        ps_ratio = price / revenue_per_share

    return ps_ratio

def sendUserInput():
    user_ticker = input("Enter the stock ticker symbol: ")
    return user_ticker

def calculate_PE_ratio(ticker):
    stock = yf.Ticker(ticker)
    pe_ratio = stock.info.get('trailingPE')
    return pe_ratio

def main():
    user_ticker = sendUserInput()

    peg = calculate_PEG(user_ticker)
    ps_ratio = calculate_PS_ratio(user_ticker)
    pe_ratio = calculate_PE_ratio(user_ticker)

    if peg is not None:
        print(f"PEG(Price/earnings to growth) Ratio: {peg:.2f}")
    else:
        print("PEG(Price/earnings to growth) Ratio not available for this stock.")

    if ps_ratio is not None:
        print(f"P/S(Price to sales) Ratio: {ps_ratio:.2f}")
    else:
        print("P/S(Price to sales) Ratio not available for this stock.")

    if pe_ratio is not None:
        print(f"P/E(Price to earnings) Ratio: {pe_ratio:.2f}")
    else:
        print("P/E(Price to earnings) Ratio not available for this stock.")
#add code in the front end to talk about how to interpret this data and ratios to perform stock analysis
if __name__ == "__main__":
    main()
