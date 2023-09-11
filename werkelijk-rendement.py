# Chapter 6 PGA
pga = 0

# Section 5.2 Result from property and debt

# Article 5.2 Result from bank deposits
bankCosts = 0
bankBenefit = 0
resultBank = bankBenefit - bankCosts

# Article 5.3 Result from real estate, via art. 3.25
realEstateCosts = 0
realEstateRent = 0
realEstateSalesProfit = 0
resultRealEstate = realEstateRent + realEstateSalesProfit - realEstateCosts

# Bunch of articles on real estate and family owned businesses

# Article 5.10 Result from other property and debt, via art. 3.25, but with yearly revaluation
# Could add costs in, but probably not that necessary
dividend = 0
stocksValue1 = 0
stocksValue0 = 0
resultStocks = dividend + stocksValue1 - stocksValue0

coupon = 0
bondsValue1 = 0
bondsValue0 = 0
resultBonds = coupon + bondsValue1 - bondsValue0

resultOtherProperty = resultBonds + resultStocks

interestPaid = 0
debtValue0 = 0
debtValue1 = 0
resultDebt = debtValue1 - debtValue0 - interestPaid

# art. 5.16 Tax free income
taxFreeIncome = 10000

# Section 5.7 Loss relief
carriedLosses = 0

# art. 5.1 Taxable income from saving and investment

# paragraph 2 Result from property and debt
resultPropertyDebt = resultBank + resultRealEstate + resultOtherProperty + resultDebt
resultPropertyDebt = max(resultPropertyDebt - taxFreeIncome, 0) - pga

# paragraph 1
taxableIncome = resultPropertyDebt - carriedLosses

# art. 2.13 Tax on taxable income
taxRate = 0.32
tax = taxRate * taxableIncome

# Return tax, and resultPropertyDebt to know carriedLosses