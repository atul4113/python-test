from datetime import date
import matplotlib.pylab as plt
from nsepy import get_history
from nsepy import get_index_pe_history

tcs = get_history(symbol='TCS',
                   start=date(2015,4,1),
                   end=date(2016,3,31))

nifty_pe = get_index_pe_history(symbol="NIFTY IT",
                                start=date(2015, 4, 1),
                                end=date(2016, 3, 31))

new_tcs=tcs["Close"]
new_nifty_pe = nifty_pe["P/E"]

plt.figure(figsize=(15,10))
plt.grid(True)

plt.plot(new_tcs,label= "Time Series TCS")
plt.show()
