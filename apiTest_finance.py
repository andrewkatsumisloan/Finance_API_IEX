
import requests
import pprint
import matplotlib.pyplot as plt
import numpy as np

pp = pprint.PrettyPrinter(indent=4)

sindex = 8

securities = ["googl", "aapl", "msft", "crm", "nvda", "amd", "fb", "spot", "tgt"]
timeSeries = "https://investors-exchange-iex-trading.p.rapidapi.com/stock/{0}/time-series".format(securities[sindex])
book = "https://investors-exchange-iex-trading.p.rapidapi.com/stock/{0}/book".format(securities[sindex])

headers = {
    'x-rapidapi-host': "investors-exchange-iex-trading.p.rapidapi.com",
    'x-rapidapi-key': "60f8a21bf8mshb884d3053d3d570p1e2a59jsn1bd1193cca7e"
    }

rTimeSeries = requests.request("GET", timeSeries, headers=headers)

pp.pprint(rTimeSeries.text)


rBook = requests.request("GET", book, headers=headers)

tlist = eval(rTimeSeries.text)
t = []
closing = []
low = []

for item in tlist:
    print(item['date'], item['close'])
    t.append(item['date'])
    closing.append(item['close'])
    low.append(item['low'])

#t = np.arange(0.0, 2.0, 0.01)
#s = 1 + np.sin(2*np.pi*t)

plt.plot(t, closing)
plt.plot(t, low)

plt.xlabel('Date (s)')
plt.ylabel('Closing Price/Low Price')
plt.title(securities[sindex])
plt.grid(True)
#plt.savefig("test.png")
plt.show()
