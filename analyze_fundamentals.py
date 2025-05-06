def analyze_stock(data):
    info = data["info"]
    financials = data["financials"]
    quarterly = data["quarterly"]
    balance = data["balance"]
    cashflow = data["cashflow"]

    results = {}

    # EPS Acceleration: simulate using fake quarterly EPS
    eps_growth = [10, 28, 56]  # Sample mockup
    results["EPS Acceleration"] = "Yes" if eps_growth[-1] > eps_growth[0] else "No"

    # Annual EPS Growth
    try:
        eps = float(info.get("trailingEps", 0))
        results["EPS Growth (Trailing 12M)"] = "Yes" if eps > 20 else "No"
    except:
        results["EPS Growth (Trailing 12M)"] = "Unknown"

    # PEG Ratio
    peg = info.get("pegRatio", None)
    results["PEG Ratio < 1.5"] = "Yes" if peg and peg < 1.5 else "No"

    # Cash Flow Health
    try:
        net_cf = float(cashflow.iloc[0][0])
        results["Positive Cash Flow"] = "Yes" if net_cf > 0 else "No"
    except:
        results["Positive Cash Flow"] = "Unknown"

    # ROE
    roe = info.get("returnOnEquity", None)
    results["ROE > 15%"] = "Yes" if roe and roe > 0.15 else "No"

    # Debt/Equity
    debt = info.get("totalDebt", 0)
    equity = info.get("totalAssets", 0) - info.get("totalLiab", 0)
    try:
        de_ratio = debt / equity
        results["Debt/Equity < 1"] = "Yes" if de_ratio < 1 else "No"
    except:
        results["Debt/Equity < 1"] = "Unknown"

    # Code 33 (mocked)
    results["Code 33 Present"] = "Yes"

    return results, []
