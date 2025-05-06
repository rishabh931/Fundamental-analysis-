import yfinance as yf

def fetch_stock_data(ticker):
    try:
        stock = yf.Ticker(f"{ticker}.NS")
        info = stock.info
        hist = stock.history(period="5y", interval="3mo")
        financials = stock.financials
        quarterly = stock.quarterly_financials
        balance = stock.balance_sheet
        cashflow = stock.cashflow
        return {
            "info": info,
            "hist": hist,
            "financials": financials,
            "quarterly": quarterly,
            "balance": balance,
            "cashflow": cashflow
        }
    except Exception as e:
        return None
