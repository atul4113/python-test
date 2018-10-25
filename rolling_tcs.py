from datetime import date
from IPython import get_ipython
import matplotlib.pylab as plt
import pandas as pd
from nsepy import get_history
# get_ipython().run_line_magic('matplotlib', 'inline')
# %matplotlib_inline

tcs = get_history(symbol='TCS',
                   start=date(2015,4,1),
                   end=date(2016,3,30))

tcs_close = pd.DataFrame(tcs.Close)

tcs_close['MA_9']= tcs_close.Close.rolling(9).mean()
tcs_close['MA_21']= tcs_close.Close.rolling(21).mean()

plt.figure(figsize=(15,10))
plt.grid(True)

plt.plot(tcs_close['Close'],label='TCS')
plt.plot(tcs_close['MA_9'],label='MA 9 Days')
plt.plot(tcs_close['MA_21'],label='MA 21 Days')

plt.legend(loc=2)
plt.show()

