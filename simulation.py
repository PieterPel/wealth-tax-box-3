import overbruggingswet
import werkelijkRendement


# Does not take intra year returns into account
def simulation(
        bankDeposits=0,
        bankPrev=0,
        percentageStocks=100 / 100,
        stocks=100000,
        stocksPrev=100000,
        bonds=0,
        bondsPrev=0,
        realEstate=0,
        debt=0,
        debtPrev=0,
        carriedLosses=0,
        years=20,
        new=True,
        taxFreeIncome=0,
        taxFreeWealth=0

):
    # Initialize
    stocksList = [stocks]
    wealth = bankDeposits + stocks + bonds + realEstate - debt
    wealthList = [wealth]
    taxList = []

    for year in range(years):

        # Calculate tax owed this year
        if new:
            tax, loss, lossRemaining = werkelijkRendement.calculate_new_tax(
                pga=0,
                bankCosts=0,
                bankValue1=bankDeposits,
                bankValue0=bankPrev,
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
                carriedLosses=carriedLosses,
                taxFreeIncome=taxFreeIncome
            )
        else:
            tax, loss, lossRemaining = overbruggingswet.calculate_old_tax(
                bankDeposits=bankDeposits,
                bonds=bonds,
                stocks=stocks,
                realEstate=0,
                taxFreeWealth=taxFreeWealth
            )

        # Update losses that are open
        carriedLosses = loss + lossRemaining

        # Bought assets
        withoutTax = 10000
        afterTax = max(withoutTax - tax, 0)

        # Sell stocks if not liquid enough
        stocksSold = abs(min(withoutTax - tax, 0))

        # Nominal Returns
        bankReturn = 0 / 100
        stocksReturn = 1 / 100
        dividend = 0 / 100
        bondsReturn = 0 / 100
        coupon = 0 / 100
        realEstateReturn = 0 / 100
        rent = 0 / 100

        # Update previous values
        bankPrev = bankDeposits
        stocksPrev = stocks
        bondsPrev = bonds
        debtPrev = debt

        # At end of year
        bankDeposits = bankDeposits * (1 + bankReturn)
        stocks = dividend + stocks * (1 + stocksReturn) + afterTax * percentageStocks - stocksSold
        bonds = coupon + bonds * (1 + bondsReturn) + afterTax * (1 - percentageStocks)
        # realEstate = rent + realEstate(realEstateReturn)  # Do real estate later, more complicated
        wealth = bankDeposits + stocks + bonds + realEstate - debt

        # Update lists
        stocksList.append(stocks)
        wealthList.append(wealth)
        taxList.append(tax)

    return wealthList, taxList, stocksList


run_new = simulation(new=True)
run_old = simulation(new=False)
print(run_new[1])
print(run_old[1])
