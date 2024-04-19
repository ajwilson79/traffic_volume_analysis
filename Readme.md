


**What is data fetching**
    This involves selecting/acquiring data from various sources like APIs, Databses, JSON file, Excel file, Web Scaraping or CSV file. 
    For this project we have used csv file https://archive.ics.uci.edu/dataset/492/metro+interstate+traffic+volume from UC Irvine Machine Learning Repository

**What is Data Exploration**
    The data exploration is done to get undatandating / insight about the selected data
    
    Typical steps involved are
    Understanding of varables of the dataset, number of rows, columns, datatypes.

    Identifing misssing values, duplicates, outliers and hanlding them.

    Understaing of Centeral tendency(Statisctics), Mean, Mode, Median and dispersion, distribution.
    
    Idetifying pattern, trends and relationships in data through visulization techniques such as histograms, scatter plots and heatmaps.

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
|date_time|Feature|Date|Hour of the data collected in local CST time||no|
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

**Mode**: The mode is the most frequently occurring value in the dataset

**Median** : The median of a dataset is the value that’s exactly in the middle when it is ordered from low to high.

**Median of an odd-numbered dataset**
For an odd-numbered dataset, find the value that lies at the (n+1)/2 position, where n is the number of values in the dataset.

**Median of an even-numbered dataset**
For an even-numbered dataset, find the two values in the middle of the dataset: the values at the n/2 and n/2+1 positions. Then, find their mean.

**Measures of Dispersion**

**Range** is difference between largest and smallest values in dataset. Range provides quick indication of variablity or spread of data points. It is sensitive to outliers.


**Variance** is the average  of squared differences from the mean Variance is measure of spread of data points around the mean. Ahigher varaince indicates that the data points are more spread around the mean, while lower vairance suggests that the data points are closer to mean.

**Stanard Deviation** is square root of variance. A higher Std. Dev. indicates greater vairablity in dataset,  a lower std. dev. suggests that data points are closer to mean.

**Interquartile Range (IQR)** IT is a measure of statistical dispersion (spred of data set)
IQR  = Q3 -Q1

    The first quartile (Q1) - It represents 25th percentile of the data.

    The third quartile (Q3) - It represents 75th percentile of the data.
IQR is amount of spread in the middle 50% of dataset. It is robust against outliers.

This dataset shows that there is high degree of variablity or scatter of data points around the mean


