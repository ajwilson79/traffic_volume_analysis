#Add this at the top of your code to import the function
# from clean_data import clean_data


import pandas as pd

def clean_data(df):
    df = df[df['rain_1h'] <= 100] 
   
    # Remove any rows with missing values
    # CURRENTLY THIS REMOVES ALL NON-HOLIDAYS
    #df.dropna(inplace=True)
   
    # Remove rows with temps lower than 200K
    df = df[df['temp'] >= 200]
    
    # Remove rows with negative traffic volume
    df = df[df['traffic_volume'] >= 0]

    # Convert 'date_time' column to datetime data type
    # and reset index
    df['date_time'] = pd.to_datetime(df['date_time'])
    df.set_index('date_time', inplace=True)
    df.sort_index(inplace=True)

    # Convert 'holiday' column to boolean indicating whether it's a holiday or not
    # NOT CURRENTLY WORKING RIGHT
    df['is_holiday'] = df['holiday'].apply(lambda x: x == 'None')
    df['is_holiday'] = df['is_holiday'].astype(bool)  # Convert to boolean type
    #df.drop(columns=['holiday'], inplace=True)  # Drop the original 'holiday' column
   
    # Return the cleaned DataFrame
    return df
