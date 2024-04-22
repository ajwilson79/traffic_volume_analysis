# Import Dependencies
import pandas as pd


# Create reference to CSV file
#csv_path = "../Resources/Metro_Interstate_Traffic_Volume.csv"
csv_path = "Metro_Interstate_Traffic_Volume.csv"
# Import the CSV into a pandas DataFrame
Traffic_Volume_df = pd.read_csv(csv_path)

Traffic_Volume_df['date_time'] = pd.to_datetime(Traffic_Volume_df['date_time'])

#Find missing date_time seuquences for every hour

min_date = Traffic_Volume_df['date_time'].min()
max_date = Traffic_Volume_df['date_time'].max()

expected_dates = pd.date_range(start=min_date, end = max_date, freq='H')

missing_dates = expected_dates[~expected_dates.isin(Traffic_Volume_df['date_time'])]

missing_dates_df = pd.DataFrame(missing_dates, columns = ['date_time'])

missing_dates_df.to_csv("missing dates.csv",  index=False)

# data created for missing dates

data ={
    'holiday':  ['None']*len(missing_dates),
    'temp': [59.0]*len(missing_dates),
    'rain_1h':[0.0]*len(missing_dates),
    'snow_1h':[0.0]*len(missing_dates),
    'clouds_all': [50]*len(missing_dates),
    'weather_main': ['clear']*len(missing_dates),
    'weather_description': ['sky is clear']*len(missing_dates),
    'date_time' : missing_dates,
    'traffic_volume':[2500]*len(missing_dates)
}
data_created_df = pd.DataFrame(data)

data_created_df .to_csv("data_created.csv", index=False)


#merge two CVSs : original data  and missing dates (data created)

merged_df = pd.concat([Traffic_Volume_df, data_created_df], ignore_index=True)

merged_df['date_time']=pd.to_datetime(merged_df['date_time'])

merged_df.sort_values(by='date_time', inplace=True)

merged_df.to_csv("merged.csv", index=False)