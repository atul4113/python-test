from datetime import date
import matplotlib.pylab as plt
from nsepy import get_history

tcs = get_history(symbol='TCS',
                   start=date(2015,4,1),
                   end=date(2016,3,31))

infy = get_history(symbol='INFY',
                   start=date(2015,4,1),
                   end=date(2016,3,31))

new_tcs=tcs["Close"]
new_infy = infy["Close"]

plt.figure(figsize=(15,10))
plt.grid(True)

plt.plot(new_tcs,label='TCS')
plt.plot(new_infy,label='INFY')

plt.legend(loc=2)
plt.show()
