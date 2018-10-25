from datetime import date
from nsepy import get_history


tcs = get_history(symbol='TCS',
                   start=date(2015,4,1),
                   end=date(2016,3,31))

infy = get_history(symbol='INFY',
                   start=date(2015,4,1),
                   end=date(2016,3,31))


l = []
def ave():
    count = 1
    pre = tcs["Volume"][0]
    for item in tcs["Volume"]:
        new = item
        deff = pre - new
        modu = abs((deff * 100) / pre)
        count += 1
        d = {}
        if modu >= 10:
            d = True
        else:
            d = False
        l.append(d)

ave()
print("Volume Shock TCS",l)


l = []
def ave():
    count = 1
    pre = tcs["Close"][0]
    for item in tcs["Close"]:
        new = item
        deff = pre - new
        modu = abs((deff * 100) / pre)
        count += 1
        d = {}
        if modu >= 2:
            d = True
        else:
            d = False
        l.append(d)

ave()
print("Price Shock of TCS",l)
print("\n")

l = []
def ave():
    count = 1
    pre = infy["Volume"][0]
    for item in infy["Volume"]:
        new = item
        deff = pre - new
        modu = abs((deff * 100) / pre)
        count += 1
        d = {}
        if modu >= 10:
            d = True
        else:
            d = False
        l.append(d)

ave()
print("Volume Shock of INFY",l)


l = []
def ave():
    count = 1
    pre = infy["Close"][0]
    for item in infy["Close"]:
        new = item
        deff = pre - new
        modu = abs((deff * 100) / pre)
        count += 1
        d = {}
        if modu >= 2:
            d = True
        else:
            d = False
        l.append(d)

ave()
print("Price Shock of INFY",l)

