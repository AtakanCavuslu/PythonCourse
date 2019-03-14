import wbdata
import datetime
import pandas as pd

# SP.URB.TOTL.IN.ZS	            Urban population (% of total)
# NY.GDP.PCAP.CD                GDP per capita (current US$)

# Gets the relevant data from wbdata
def getData():
    data_date = datetime.datetime(2010, 1, 1)
    x = wbdata.get_data("NY.GDP.PCAP.CD", data_date = data_date, pandas = True)
    y = wbdata.get_data("SP.URB.TOTL.IN.ZS", data_date = data_date, pandas = True)
    data = pd.concat([x, y], axis = 1)
    # Drop the NaN values
    data = data.dropna(axis=0, how='any')
    data.columns = ["gdp", "urbanPop"]
    x = data["gdp"].tolist()
    y = data["urbanPop"].tolist()
    return (x, y)
