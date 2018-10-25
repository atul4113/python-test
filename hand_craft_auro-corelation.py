from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from datetime import date
from matplotlib import pyplot
from nsepy import get_history

tcs = get_history(symbol='TCS',
                   start=date(2015,4,1),
                   end=date(2016,3,31))

infy = get_history(symbol='INFY',
                   start=date(2015,4,1),
                   end=date(2016,3,31))
plot_acf(tcs["Close"])
plot_acf(infy["Close"])
pyplot.show()

plot_pacf(tcs["Close"], lags=50)
plot_pacf(infy["Close"], lags=50)
pyplot.show()