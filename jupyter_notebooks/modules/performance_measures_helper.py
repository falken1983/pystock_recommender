#!/usr/bin/env python3

import pandas as pd
import numpy as np

scalers = {
    "daily": 252,
    "monthly": 12,
    "weekly": 50,
    "biweekly": 25
}

""" 
Performance Measures Related Functions
"""

#Sharpe Ratio Functions
def sharpe_ratio(y, freq="daily"):
    """Classical Sharpe Ratio. Annualized Ratio
    """    
    # Annualized ratio
    return np.sqrt(scalers[freq]) * (y.mean() / y.std()) 

#TBD
def israelsen_sharpe_ratio(y, freq="daily"):    
    """Israelsen Trick for the Sharpe Ratio
    """
    if y.mean()<0:
        return np.sqrt(scalers[freq]) *(y.mean()*y.std())
    else:
        return sharpe_ratio(y)

#Returns Related Functions
def multi_period_return(period_returns):
    return np.prod(period_returns + 1) - 1

def net_cumreturn(data, last_row=False):
    """Net Cumulative Returns
    """
    df = ((1+data).cumprod(axis=0)-1)
    if last_row:
        return df.iloc[-1]
    return df

""" 
Scoring Related Functions
"""
def scorer(data, bins=20):
    """ Simple Scorer (The Higher, the Better) """
    df = pd.cut(x=data, bins=bins, labels=False)
    return 1+df

def main():
    pass

if __name__ == "__main__":
    main()