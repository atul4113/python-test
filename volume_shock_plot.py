from datetime import date
import matplotlib.pylab as plt
from nsepy import get_history

tcs = get_history(symbol='TCS',
                   start=date(2015,4,1),
                   end=date(2016,3,31))

infy = get_history(symbol='INFY',
                   start=date(2015,4,1),
                   end=date(2016,3,31))

l_tcs_vol = []
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
        l_tcs_vol.append(d)

ave()

l_infy_vol = []
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
        l_infy_vol.append(d)

ave()

plt.figure(figsize=(15,1))
plt.grid(True)

plt.plot(tcs.index,l_tcs_vol, label='TCS')
plt.plot(tcs.index,l_infy_vol,label='INFY')

plt.legend(loc=2)
plt.show()