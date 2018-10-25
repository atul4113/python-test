from datetime import date
import matplotlib.pylab as plt
from nsepy import get_history

tcs = get_history(symbol='TCS',
                   start=date(2015,4,1),
                   end=date(2016,3,31))

infy = get_history(symbol='INFY',
                   start=date(2015,4,1),
                   end=date(2016,3,31))

l_tcs_close = []
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
        l_tcs_close.append(d)

ave()


l_infy_close = []
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
        l_infy_close.append(d)

ave()

plt.figure(figsize=(15,10))
plt.grid(True)

plt.plot(tcs.index,l_tcs_close, label='TCS')
plt.plot(tcs.index,l_infy_close,label='INFY')

plt.legend(loc=2)
plt.show()
