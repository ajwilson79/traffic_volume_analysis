# Import Dependencies
import pandas as pd


# Create reference to CSV file
#csv_path = "../Resources/Metro_Interstate_Traffic_Volume.csv"
csv_path = "Metro_Interstate_Traffic_Volume.csv"

# Import the CSV into a pandas DataFrame
Traffic_Volume_df = pd.read_csv(csv_path)

Traffic_Volume_df['date_time'] = pd.to_datetime(Traffic_Volume_df['date_time'])
print (Traffic_Volume_df.dtypes)

#remve duplicates for coulmn "date_time"
# print(Traffic_Volume_df.count())

# duplicates = Traffic_Volume_df[Traffic_Volume_df.duplicated('date_time')]

# print ("no. of duplicates:" , len(duplicates))

# Traffic_Volume_df.drop_duplicates('date_time', inplace=True)
# Traffic_Volume_df.to_csv("duplicates_removed.csv", index=False)

# print(Traffic_Volume_df.count())

# #drop duplicates
# Traffic_Volume_df.drop_duplicates(inplace=True)
# Traffic_Volume_df.to_csv("duplicates_removed.csv", index=False)
# #check row count after dropping duplicates
# Traffic_Volume_df.count()

#correct "holiday" column
#Traffic_Volume_df = pd.to_datetime(Traffic_Volume_df['date_time'])
for index, row in Traffic_Volume_df.iterrows():
    #if no18bede6c-af04-4dd8-9eb7-a4f8d1cda498t pd.isnull(row['holiday']):
    #if  row['holiday'] !='None':
    if pd.notna(row['holiday']):
        holiday_value = row['holiday']

        for i in range (1,50):

            if index + i < len(Traffic_Volume_df):
                # print("Curret date", Traffic_Volume_df.at[index+i, 'date_time'].date())
                # print("Previous date", Traffic_Volume_df.at[index, 'date_time'].date() )

                if Traffic_Volume_df.at[index+i, 'date_time'].date() == Traffic_Volume_df.at[index, 'date_time'].date() :

                    Traffic_Volume_df.at[index+i, 'holiday'] = holiday_value
           

            else: 
          
                break
Traffic_Volume_df.to_csv("data_cleanup.csv", index=False)

#remve duplicates for coulmn "date_time"
print(Traffic_Volume_df.count())

duplicates = Traffic_Volume_df[Traffic_Volume_df.duplicated('date_time')]

print ("no. of duplicates:" , len(duplicates))

Traffic_Volume_df.drop_duplicates('date_time', inplace=True)
Traffic_Volume_df.to_csv("duplicates_removed.csv", index=False)

# print(Traffic_Volume_df.count())