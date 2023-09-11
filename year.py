import overbruggingswet
import werkelijkRendement

# Does not adjust for intra year returns

# Params
bankDeposits = 0
percentageStocks = 100 / 100
stocks = 100000
stocksPrev = 100000
bonds = 0
bondsPrev = 0
realEstate = 0
realEstatePrev = 0
debt = 0
debtPrev = 0
carriedLosses = 0
years = 20
new = False

for year in range(years):

    # Calculate tax owed this year
    if new:
        tax, loss, lossRemaining = werkelijkRendement.calculate_new_tax(
            pga=0,
            bankCosts=0,
            bankBenefit=0,
            realEstateCosts=0,
            realEstateRent=0,
            realEstateSalesProfit=0,
            dividend=0,
            stocksValue1=stocks,
            stocksValue0=stocksPrev,
            coupon=0,
            bondsValue1=bonds,
            bondsValue0=bondsPrev,
            interestPaid=0,
            debtValue1=debt,
            debtValue0=debtPrev,
            carriedLosses=carriedLosses
            )
    else:
        tax, loss, lossRemaining = overbruggingswet.calculate_old_tax(
            bankDeposits=bankDeposits,
            bonds=bonds,
            stocks=stocks,
            realEstate=0
        )

    # Update losses that are open
    carriedLosses = loss + lossRemaining

    # Bought assets
    withoutTax = 10000
    afterTax = max(withoutTax - tax, 0)

    # Sell stocks if not liquid enough
    stocksSold = min(withoutTax - tax, 0)

    # Nominal Returns
    stocksReturn = 10/100
    dividend = 0/100
    bondsReturn = 0/100
    coupon = 0/100
    # realEstateReturn = 0/100
    # rent = 0/100

    # Update previous values
    stocksPrev = stocks
    bondsPrev = bonds
    realEstatePrev = realEstate
    debtPrev = debt

    # At end of year
    stocks = dividend + stocks * (1 + stocksReturn) + afterTax * percentageStocks - stocksSold
    bonds = coupon + bonds * (1 + bondsReturn) + afterTax * (1-percentageStocks)
    # realEstate = rent + realEstate(realEstateReturn)  # Do real estate later, more complicated

print(stocks, tax)
