


**What is data fetching**
    This involves selecting/acquiring data from various sources like APIs, Databses, JSON file, Excel file, Web Scaraping or CSV file. 
    For this project we have used csv file https://archive.ics.uci.edu/dataset/492/metro+interstate+traffic+volume from UC Irvine Machine Learning Repository

**What is Data Exploration**
 The data exploration is done to get undatandating / insight about the selected data
    
- Typical steps involved are
    Understanding of varables of the dataset, number of rows, columns, datatypes.

- Identifing misssing values, duplicates, outliers and hanlding them.

- Understaing of Centeral tendency(Statisctics), Mean, Mode, Median and dispersion, distribution.
    
- Idetifying pattern, trends and relationships in data through visulization techniques such as histograms, scatter plots and heatmaps.

|**Variables Table**||||||
|---|---|---|---|---|---|
|**Variable Name**|**Role**|**Type**|**Description**|**Units**|**Missing Values**|
|holiday|Feature|Categorical|US National holidays plus regional holiday Minnesota State Fair| ||no|
|temp|Feature|Continuous|Average temp in kelvin|Kelvin|no|
|rain_1h|Feature|Continuous|Amount in mm of rain that occurred in the hour|mm|no|
|snow_1h|Feature|Continuous|Amount in mm of snow that occurred in the hour|mm|no|
|clouds_all|Feature|Integer|Percentage of cloud cover|%|no|
|weather_main|Feature|Categorical|Short textual description of the current weather||no|
|weather_description|Feature|Categorical|Longer textual description of the current weather||no|
|date_time|Feature|Date|Hour of the data collected in local CST time||Yes|
|traffic_volume|Target|Integer|Hourly I-94 ATR 301 reported westbound traffic volume||no|

**Variable Types :**

- **Categorial Variable** : Categorical Variables represent categories or groups. It can take fixed number of possible values to represent qualtative characteristics.

- **Continuous Variable** : Continous Variables are numeric vaiables. These values can be fractional or decimal.

- **Integer Variables** : Integer Variables are numeric. These values can be only integers.

- **Date Variable** : Date vaiable in this context repsents date and time.

**Dataset Characteristics :**
    Multivariate, Sequential, Time-Series

- **Multivarate** : A Multivariate dataset contains mutliple variables(features or attributes) for each data points. Each variable (feature or attribute) representing different aspect or characteristics of data.

- **Sequential** : A equential dataset consists of data points that are arranged in a specific sequence or time series. Each data point respresents an observation(data point) capatured at time intervals

- **Time-Series** : A Time Series dataset represents obseravation (data point) collected at equally spaced time intervals.

Other types of dataset that exists are Sptial Dataset (features observed across various regions, locations), Image dataset (digial or visual data stored in matrix format), Text Dataset (textual data or document, such as cutsomer reivews).

**Role of a variable**

- **Feaute** is indepdent variable (input varible or predictor).These are used to make predictions or model relationships

- **Target** is dedependent variable(response variabel or output variable ) that machine learning model seeks to predict or explain.



**Central Tendency**
Central tendency is defined as “the statistical measure that identifies a single value as representative of an entire distribution. It aims to provide an accurate description of the entire data. It is the single value that is most typical/representative of the collected data. 
It lets us know what is normal or 'average' for a set of data. It also condenses the data set down to one representative value, which is useful when you are working with large amounts of data.

- **Mode**: The mode is the most frequently occurring value in the dataset

- **Median** : The median of a dataset is the value that’s exactly in the middle when it is ordered from low to high.

- **Median of an odd-numbered dataset**
For an odd-numbered dataset, find the value that lies at the (n+1)/2 position, where n is the number of values in the dataset.

- **Median of an even-numbered dataset**
For an even-numbered dataset, find the two values in the middle of the dataset: the values at the n/2 and n/2+1 positions. Then, find their mean.

- **Mean**
 The arithmetic mean of a dataset (which is different from the geometric mean) is the sum of all values divided by the total number of values.

- **Distribution**
If the mean is approximately equal to the median, the distributionis symmetrical
if the mean is greater than the median, the distributino is positively skewed.
If the mean is less that the media, the distribution is negative skewed.

**Measures of Dispersion**

- **Range** is difference between largest and smallest values in dataset. Range provides quick indication of variablity or spread of data points. It is sensitive to outliers.


- **Variance** is the average  of squared differences from the mean Variance is measure of spread of data points around the mean. Ahigher varaince indicates that the data points are more spread around the mean, while lower vairance suggests that the data points are closer to mean.

- **Stanard Deviation** is square root of variance. A higher Std. Dev. indicates greater vairablity in dataset,  a lower std. dev. suggests that data points are closer to mean.

- **Interquartile Range (IQR)** IT is a measure of statistical dispersion (spred of data set)
IQR  = Q3 -Q1

    The first quartile (Q1) - It represents 25th percentile of the data.

    The third quartile (Q3) - It represents 75th percentile of the data.
IQR is amount of spread in the middle 50% of dataset. It is robust against outliers.

    **This dataset shows that there is high degree of variablity or scatter of data points around the mean**

**Indtentifaction and Handling of missing data**
1. **Missing Holidays :** 
Holiday values are present only at 00:00 hour of the date, missing at other hours for the date.
For example,

| holiday      | date_time       | traffic_volume |
|--------------|-----------------|----------------|
| Columbus Day | 10/8/2012 0:00  | 455            |
| None         | 10/8/2012 1:00  | 336            |
| None         | 10/8/2012 2:00  | 265            |
| None         | 10/8/2012 3:00  | 314            |
| None         | 10/8/2012 4:00  | 779            |
| None         | 10/8/2012 5:00  | 2571           |
| None         | 10/8/2012 6:00  | 5563           |
| None         | 10/8/2012 7:00  | 6676           |
| None         | 10/8/2012 8:00  | 5966           |
| None         | 10/8/2012 9:00  | 4832           |
| None         | 10/8/2012 10:00 | 4395           |
| None         | 10/8/2012 11:00 | 4411           |
| None         | 10/8/2012 12:00 | 4648           |
| None         | 10/8/2012 13:00 | 4602           |
| None         | 10/8/2012 14:00 | 5125           |
| None         | 10/8/2012 15:00 | 5502           |
| None         | 10/8/2012 16:00 | 5979           |
| None         | 10/8/2012 17:00 | 5663           |
| None         | 10/8/2012 18:00 | 4259           |
| None         | 10/8/2012 19:00 | 3069           |
| None         | 10/8/2012 20:00 | 2378           |
| None         | 10/8/2012 21:00 | 2030           |
| None         | 10/8/2012 22:00 | 1400           |
| None         | 10/8/2012 23:00 | 917            |

**Handling of missing holiday data**
Created following code 

 ```python
 #Holiday Cleanup. Fill up values for missing holiday values.
#Also, saves output in data_cleanup.csv for manual validation
# It will take some time for execution completion # 
for index, row in Traffic_Volume_df.iterrows():
 
      if pd.notna(row['holiday']):
        holiday_value = row['holiday']

        for i in range (1,50):

            if index + i < len(Traffic_Volume_df):
               
                if Traffic_Volume_df.at[index+i, 'date_time'].date() == Traffic_Volume_df.at[index, 'date_time'].date() :

                    Traffic_Volume_df.at[index+i, 'holiday'] = holiday_value
           

            else: 
          
                break
Traffic_Volume_df.to_csv("data_cleanup.csv", index=False)
 ```
After running code above code

| holiday      | date_time       | traffic_volume |
|--------------|-----------------|----------------|
| Columbus Day | 10/8/2012 0:00  | 455            |
| Columbus Day | 10/8/2012 1:00  | 336            |
| Columbus Day | 10/8/2012 2:00  | 265            |
| Columbus Day | 10/8/2012 3:00  | 314            |
| Columbus Day | 10/8/2012 4:00  | 779            |
| Columbus Day | 10/8/2012 5:00  | 2571           |
| Columbus Day | 10/8/2012 6:00  | 5563           |
| Columbus Day | 10/8/2012 7:00  | 6676           |
| Columbus Day | 10/8/2012 8:00  | 5966           |
| Columbus Day | 10/8/2012 9:00  | 4832           |
| Columbus Day | 10/8/2012 10:00 | 4395           |
| Columbus Day | 10/8/2012 11:00 | 4411           |
| Columbus Day | 10/8/2012 12:00 | 4648           |
| Columbus Day | 10/8/2012 13:00 | 4602           |
| Columbus Day | 10/8/2012 14:00 | 5125           |
| Columbus Day | 10/8/2012 15:00 | 5502           |
| Columbus Day | 10/8/2012 16:00 | 5979           |
| Columbus Day | 10/8/2012 17:00 | 5663           |
| Columbus Day | 10/8/2012 18:00 | 4259           |
| Columbus Day | 10/8/2012 19:00 | 3069           |
| Columbus Day | 10/8/2012 20:00 | 2378           |
| Columbus Day | 10/8/2012 21:00 | 2030           |
| Columbus Day | 10/8/2012 22:00 | 1400           |
| Columbus Day | 10/8/2012 23:00 | 917            |

**Missing  hour sequences for a paricular date**
The following code will identify missing hour sequences and create "missing dates.csv" for manual data validation.
 ```python
 csv_path = "Metro_Interstate_Traffic_Volume.csv"
# Import the CSV into a pandas DataFrame
Traffic_Volume_df = pd.read_csv(csv_path)

Traffic_Volume_df['date_time'] = pd.to_datetime(Traffic_Volume_df['date_time'])

#Find miising date_time seuquences for every hour

min_date = Traffic_Volume_df['date_time'].min()
max_date = Traffic_Volume_df['date_time'].max()

expected_dates = pd.date_range(start=min_date, end = max_date, freq='H')

missing_dates = expected_dates[~expected_dates.isin(Traffic_Volume_df['date_time'])]

missing_dates_df = pd.DataFrame(missing_dates, columns = ['date_time'])

missing_dates_df.to_csv("missing dates.csv",  index=False)
```
Using above code, missing hour sequece can be found out.
| Orignal Sequence |  | Missing Sequence |
|------------------|--|------------------|
| 9/21/2017 0:00   |  |                  |
| 9/21/2017 1:00   |  |                  |
| 9/21/2017 2:00   |  |                  |
| 9/21/2017 3:00   |  |                  |
| 9/21/2017 4:00   |  |                  |
| 9/21/2017 5:00   |  |                  |
| 9/21/2017 6:00   |  |                  |
| 9/21/2017 7:00   |  |                  |
| 9/21/2017 8:00   |  |                  |
| 9/21/2017 9:00   |  |                  |
| 9/21/2017 13:00  |  | 9/21/2017 10:00  |
| 9/21/2017 14:00  |  | 9/21/2017 11:00  |
| 9/21/2017 15:00  |  | 9/21/2017 12:00  |
| 9/21/2017 16:00  |  |                  |
| 9/21/2017 17:00  |  |                  |
| 9/21/2017 18:00  |  |                  |
| 9/21/2017 19:00  |  |                  |
| 9/21/2017 20:00  |  |                  |
| 9/21/2017 21:00  |  |                  |
| 9/21/2017 22:00  |  |                  |
| 9/21/2017 23:00  |

Data can be manufactured to fill in missing data.
For example,
```python
data created for missing dates

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
```
Example of data created for missing hour sequence 

| holiday | temp | rain_1h | snow_1h | clouds_all | weather_main | weather_description | date_time       | traffic_volume |
|---------|------|---------|---------|------------|--------------|---------------------|-----------------|----------------|
| None    | 294  | 0       | 0       | 50         | clear        | sky is clear        | 9/21/2017 10:00 | 2500           |
| None    | 294  | 0       | 0       | 50         | clear        | sky is clear        | 9/21/2017 11:00 | 2500           |
| None    | 294  | 0       | 0       | 50         | clear        | sky is clear        | 9/21/2017 12:00 | 2500           |

A new CSV / dataframe can be created to by merging to CSVs ( orignal CSV and data created for missing CSV)
```python
#merge two CVSs : original data  and missing dates (data created)

merged_df = pd.concat([Traffic_Volume_df, data_created_df], ignore_index=True)

merged_df['date_time']=pd.to_datetime(merged_df['date_time'])

merged_df.sort_values(by='date_time', inplace=True)

merged_df.to_csv("merged.csv", index=False)
```
For example:
| holiday | temp   | rain_1h | snow_1h | clouds_all | weather_main | weather_description | date_time       | traffic_volume |
|---------|--------|---------|---------|------------|--------------|---------------------|-----------------|----------------|
| None    | 284.42 | 0       | 0       | 1          | Clear        | sky is clear        | 9/21/2017 0:00  | 686            |
| None    | 284.22 | 0       | 0       | 1          | Mist         | mist                | 9/21/2017 1:00  | 404            |
| None    | 284    | 0       | 0       | 1          | Clear        | sky is clear        | 9/21/2017 2:00  | 297            |
| None    | 283.07 | 0       | 0       | 1          | Mist         | mist                | 9/21/2017 3:00  | 340            |
| None    | 282.29 | 0       | 0       | 1          | Mist         | mist                | 9/21/2017 4:00  | 907            |
| None    | 282.21 | 0       | 0       | 1          | Mist         | mist                | 9/21/2017 5:00  | 3055           |
| None    | 282    | 0       | 0       | 1          | Mist         | mist                | 9/21/2017 6:00  | 5596           |
| None    | 282.08 | 0       | 0       | 5          | Fog          | fog                 | 9/21/2017 7:00  | 6133           |
| None    | 282.74 | 0       | 0       | 5          | Mist         | mist                | 9/21/2017 8:00  | 6143           |
| None    | 286.71 | 0       | 0       | 1          | Clear        | sky is clear        | 9/21/2017 9:00  | 5722           |
| None    | 294    | 0       | 0       | 50         | clear        | sky is clear        | 9/21/2017 10:00 | 2500           |
| None    | 294    | 0       | 0       | 50         | clear        | sky is clear        | 9/21/2017 11:00 | 2500           |
| None    | 294    | 0       | 0       | 50         | clear        | sky is clear        | 9/21/2017 12:00 | 2500           |
| None    | 297.01 | 0       | 0       | 5          | Clear        | sky is clear        | 9/21/2017 13:00 | 4378           |
| None    | 298.08 | 0       | 0       | 1          | Clear        | sky is clear        | 9/21/2017 14:00 | 4926           |
| None    | 299.29 | 0       | 0       | 5          | Clear        | sky is clear        | 9/21/2017 15:00 | 5823           |
| None    | 300.15 | 0       | 0       | 20         | Clouds       | few clouds          | 9/21/2017 16:00 | 6899           |
| None    | 300.72 | 0       | 0       | 20         | Clouds       | few clouds          | 9/21/2017 17:00 | 6533           |
| None    | 300.72 | 0       | 0       | 1          | Clear        | sky is clear        | 9/21/2017 18:00 | 5174           |
| None    | 300.01 | 0       | 0       | 20         | Clouds       | few clouds          | 9/21/2017 19:00 | 3929           |
| None    | 299.02 | 0       | 0       | 1          | Clear        | sky is clear        | 9/21/2017 20:00 | 3442           |
| None    | 298.55 | 0       | 0       | 75         | Clouds       | broken clouds       | 9/21/2017 21:00 | 3936           |
| None    | 298.02 | 0       | 0       | 40         | Clouds       | scattered clouds    | 9/21/2017 22:00 | 2423           |
| None    | 297.75 | 0       | 0       | 1          | Clear        | sky is clear        | 9/21/2017 23:00 | 1293           |

For python code, refer "Missing date sequence.py" python program.
Need do data cleanup again for this file.

**Pros and Cons of manufacturing data to fill in missing data**

- **Pros** Completeness, Preserves structure

- **Cons** Not real data, leading to bias, Incorrect results.

**We have decided not use manufactured data for this assignment**

**Remove duplicates for date_time**
If date_time and traffic_volume combiation is same, it is considered as duplicate for this assignment.

| holiday | temp   | rain_1h | snow_1h | clouds_all | weather_main | weather_description     | date_time        | traffic_volume |
|---------|--------|---------|---------|------------|--------------|-------------------------|------------------|----------------|
| NaN     | 51.692 | 0       | 0       | 93         | Mist         | mist                    | 10/14/2012 14:00 | 4358           |
| NaN     | 51.692 | 0       | 0       | 93         | Rain         | light rain              | 10/14/2012 14:00 | 4358           |
| NaN     | 51.692 | 0       | 0       | 93         | Drizzle      | light intensity drizzle | 10/14/2012 14:00 | 4358           |

```python
#remove duplicates for coulmn "date_time"
print("Before duplictes removal\n", Traffic_Volume_df.count())

duplicates = Traffic_Volume_df[Traffic_Volume_df.duplicated('date_time')]

print ("no. of duplicates:" , len(duplicates))

Traffic_Volume_df.drop_duplicates('date_time', inplace=True)
Traffic_Volume_df.to_csv("duplicates_removed.csv", index=False)
print("After duplictes removal\n", Traffic_Volume_df.count())
```

duplicates are remvoed, for example:

| holiday | temp   | rain_1h | snow_1h | clouds_all | weather_main | weather_description | date_time        | traffic_volume |
|---------|--------|---------|---------|------------|--------------|---------------------|------------------|----------------|
| NaN     | 51.692 | 0       | 0       | 93         | Mist         | mist                | 10/14/2012 14:00 | 4358           |


