def calculate_new_tax(
        pga=0,
        bankCosts=0,
        bankValue1=0,
        bankValue0=0,
        realEstateCosts=0,
        realEstateRent=0,
        realEstateSalesProfit=0,
        dividend=0,
        stocksValue1=0,
        stocksValue0=0,
        coupon=0,
        bondsValue1=0,
        bondsValue0=0,
        interestPaid=0,
        debtValue1=0,
        debtValue0=0,
        taxFreeIncome=10000,
        carriedLosses=0,
        taxRate=0.32

):

    # Chapter 6 PGA
    pga = pga

    # Section 5.2 Result from property and debt

    # Article 5.2 Result from bank deposits
    resultBank = bankValue1 - bankValue0 - bankCosts

    # Article 5.3 Result from real estate, via art. 3.25
    resultRealEstate = realEstateRent + realEstateSalesProfit - realEstateCosts

    # Bunch of articles on real estate and family owned businesses

    # Article 5.10 Result from other property and debt, via art. 3.25, but with yearly revaluation
    # Could add costs in, but probably not that necessary
    resultStocks = dividend + stocksValue1 - stocksValue0

    resultBonds = coupon + bondsValue1 - bondsValue0

    resultOtherProperty = resultBonds + resultStocks

    resultDebt = debtValue1 - debtValue0 - interestPaid

    # art. 5.16 Tax free income
    taxFreeIncome = taxFreeIncome

    # Section 5.7 Loss relief
    carriedLosses = carriedLosses

    # art. 5.1 Taxable income from saving and investment

    # paragraph 2 Result from property and debt
    resultPropertyDebt = resultBank + resultRealEstate + resultOtherProperty + resultDebt

    if resultPropertyDebt > 0:
        resultPropertyDebt = max(resultPropertyDebt - taxFreeIncome, 0) - pga
    else:
        resultPropertyDebt = resultPropertyDebt - pga

    # paragraph 1
    lossesUsed = min(carriedLosses, resultPropertyDebt)
    taxableIncome = resultPropertyDebt - lossesUsed

    # art. 2.13 Tax on taxable income
    tax = taxRate * taxableIncome

    # Return tax owed, loss of this year, and loss that is still open
    return tax, abs(min(resultPropertyDebt, 0)), carriedLosses - lossesUsed
