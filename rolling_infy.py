from datetime import date

from IPython import get_ipython
import matplotlib.pylab as plt
import pandas as pd
from nsepy import get_history
# get_ipython().run_line_magic('matplotlib', 'inline')

infy = get_history(symbol='INFY',
                   start=date(2015,4,1),
                   end=date(2016,3,30))

infy_close = pd.DataFrame(infy.Close)

infy_close['MA_9']= infy_close.Close.rolling(9).mean()
infy_close['MA_21']= infy_close.Close.rolling(21).mean()

plt.figure(figsize=(15,10))
plt.grid(True)

plt.plot(infy_close['Close'],label='INFY')
plt.plot(infy_close['MA_9'],label='MA 9 Days')
plt.plot(infy_close['MA_21'],label='MA 21 Days')

plt.legend(loc=2)
plt.show()
