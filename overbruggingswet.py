def calculate_old_tax(bankDeposits=0,
                      debt=0,
                      bonds=0,
                      stocks=0,
                      realEstate=0,
                      taxFreeWealth=57000,
                      savingsRate=0.01/100,
                      debtRate=2.46/100,
                      otherRate=6.17/100,
                      pga=0,
                      taxRate=0.32
                      ):
    # art. 5.3 Return base
    other = bonds + stocks + realEstate

    returnBase = bankDeposits + other - debt

    # art. 5.5 Tax Free Wealth
    taxFreeWealth = taxFreeWealth

    # art. 5.2 Gain from saving and investing

    # paragraph 1 Base saving and investing
    baseSI = max(returnBase - taxFreeWealth, 0)

    # paragraph 2 Effective return percentage
    Return = savingsRate * bankDeposits + debtRate * debt + otherRate * other

    effReturnPct = Return / returnBase

    # paragraph 1
    gain = effReturnPct * baseSI

    # Chapter 6: PGA
    pga = pga

    # art. 5.1 Taxable income from saving and investing
    taxableIncome = gain - pga

    # art. 2.13 Tax on taxable income
    tax = taxRate * taxableIncome

    # Chapter 8 Heffingskorting
    # For now assume that it all goes to box 1 income

    return tax
