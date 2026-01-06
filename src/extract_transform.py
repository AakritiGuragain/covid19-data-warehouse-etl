import pandas as pd

#Read data from CSV file
confirmed= pd.read_csv('data/time_series_covid19_confirmed_global.csv')
deaths= pd.read_csv('data/time_series_covid19_deaths_global.csv')
recovered= pd.read_csv('data/time_series_covid19_recovered_global.csv')

#Transform data from wide to long format
def melt_data(df, value_name):
    return df.melt(
        id_vars=['Country/Region'],
        var_name='Date',
        value_name=value_name
    )

confirmed_long = melt_data(confirmed, 'Confirmed')
deaths_long = melt_data(deaths, 'Deaths')
recovered_long = melt_data(recovered, 'Recovered')

#Merge datasets on Country/Region and Date
covid_df= confirmed_long.merge(deaths_long, on=['Country/Region', 'Date']).merge(
    recovered_long, on=['Country/Region', 'Date']
)