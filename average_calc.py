from datetime import date
import statistics as sta
from nsepy import get_history
from nsepy import get_index_pe_history

tcs = get_history(symbol='TCS',
                   start=date(2015,4,1),
                   end=date(2016,3,31))

infy = get_history(symbol='INFY',
                   start=date(2015,4,1),
                   end=date(2016,3,31))

nifty_pe = get_index_pe_history(symbol="NIFTY IT",
                                start=date(2015, 4, 1),
                                end=date(2016, 3, 31))

avr_tcs = tcs['Close']
avr_infy = infy['Close']
avr_nifty_pe = nifty_pe['P/E']
avr_nifty_pb = nifty_pe['P/B']
avr_nifty_div = nifty_pe['Div Yield']

date_index = tcs.index
def average():
    count = 0
    for x in date_index:
        if x <= date(2016, 4, 30):
            count += 1
    tcs_av = sta.mean(avr_tcs.head(count))
    infy_av = sta.mean(avr_infy.head(count))
    nifty_av_pe = sta.mean(avr_nifty_pe.head(count))
    nifty_av_pb = sta.mean(avr_nifty_pb.head(count))
    nifty_av_div = sta.mean(avr_nifty_div.head(count))
    print("Average of April ")
    print("TCS : ",tcs_av)
    print("INFY :",infy_av)
    print("NIFTY P/E :",nifty_av_pe)
    print("NIFTY P/B :",nifty_av_pb)
    print("NIFTY Div Yield :",nifty_av_div)
    print("\n")

    for x in date_index:
        if x <= date(2016, 7, 30):
            count += 1
    tcs_av = sta.mean(avr_tcs.head(count))
    infy_av = sta.mean(avr_infy.head(count))
    print("Average of 4 Months April,May,June,July ")
    print("TCS : ", tcs_av)
    print("INFY :", infy_av)
    print("NIFTY P/E :", nifty_av_pe)
    print("NIFTY P/B :", nifty_av_pb)
    print("NIFTY Div Yield :", nifty_av_div)
    print("\n")

    for x in date_index:
        if x <= date(2016, 11, 30):
            count += 1
    tcs_av = sta.mean(avr_tcs.head(count))
    infy_av = sta.mean(avr_infy.head(count))
    print("Average of 8 Months")
    print("TCS : ", tcs_av)
    print("INFY :", infy_av)
    print("NIFTY P/E :", nifty_av_pe)
    print("NIFTY P/B :", nifty_av_pb)
    print("NIFTY Div Yield :", nifty_av_div)
    print("\n")

    for x in date_index:
        if x <= date(2017, 3, 31):
            count += 1
    tcs_av = sta.mean(avr_tcs.head(count))
    infy_av = sta.mean(avr_infy.head(count))
    print("Average of 12 Months")
    print("TCS : ", tcs_av)
    print("INFY :", infy_av)
    print("NIFTY P/E :",nifty_av_pe)
    print("NIFTY P/B :",nifty_av_pb)
    print("NIFTY Div Yield :",nifty_av_div)

average()
# print(avr_tcs)
# print(statistics.mean(avr_tcs))
# print(statistics.mean(avr_tcs_all))
