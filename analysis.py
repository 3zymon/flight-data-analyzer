import pandas as pd
import numpy as np

# LOAD DATA
df = pd.read_csv("data/flights_2025_01.csv")

# INITIAL INSPECTION
print('1. INITIAL INSPECTION')

print(df.head())
print(df.shape)
print(df.dtypes)

df.info()

print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())

# MISSING VALUES INVESTIGATION
print('2. MISSING VALUES INVESTIGATION')

cancelled_flights = df['CANCELLED'].sum()
non_cancelled_flights_missing_arr_delay = (df['ARR_DELAY'].isnull() & (df['CANCELLED'] == 0)).sum()
non_cancelled_flights_missing_air_time = (df['AIR_TIME'].isnull() & (df['CANCELLED'] == 0)).sum()
missing_air_time_and_arr_delay = (df['AIR_TIME'].isnull() & df['ARR_DELAY'].isnull()).sum()
non_cancelled_flights_diverted_missing_air_time = ((df['CANCELLED'] == 0) & (df['DIVERTED'] == 1) & df['AIR_TIME'].isnull()).sum()
non_cancelled_flights_diverted_missing_arr_delay = ((df['CANCELLED'] == 0) & (df['DIVERTED'] == 1) & df['ARR_DELAY'].isnull()).sum()
cancelled_and_diverted_flights = ((df['CANCELLED'] == 1) & (df['DIVERTED'] == 1)).sum()
cancelled_flights_missing_dep_delay = ((df['CANCELLED'] == 1) & (df['DEP_DELAY'].isnull())).sum()
non_cancelled_flights_missing_dep_delay = ((df['CANCELLED'] == 0) & (df['DEP_DELAY'].isnull())).sum()
cancelled_flights_missing_dep_and_arr_delay = ((df['CANCELLED'] == 1) & df['DEP_DELAY'].isnull() & df['ARR_DELAY'].isnull()).sum()
cancelled_flights_missing_arr_delay = ((df['CANCELLED'] == 1) & df['ARR_DELAY'].isnull()).sum()

print(f'Cancelled flights: {cancelled_flights}')
print(f'Non-cancelled flights missing ARR_DELAY: {non_cancelled_flights_missing_arr_delay}')

# DATA CLEANING
print('3. DATA CLEANING')

df['FL_DATE'] = pd.to_datetime(
    df['FL_DATE'],
    format='%m/%d/%Y %I:%M:%S %p',
)
print(df['FL_DATE'].dtype)

# Missing values are kept because they represent cancelled/diverted flights.

counts = df.value_counts()
counts[counts >= 2]
print(counts.head())
counts = df.value_counts(dropna=False)
print(counts.value_counts())
print(df[df.duplicated(keep=False)].head(10))
df = df.drop_duplicates()
print(df.duplicated().sum())

# EXPLORATORY ANALYSIS
print('4. EXPLORATORY ANALYSIS')
# Average departure delay by day of week
day_of_week_dep_delay = df.groupby('DAY_OF_WEEK')['DEP_DELAY'].mean()
min_day_dep_delay = day_of_week_dep_delay.min()
min_day_dep_delay_name = day_of_week_dep_delay.idxmin()
max_day_dep_delay = day_of_week_dep_delay.max()
max_day_dep_delay_name = day_of_week_dep_delay.idxmax()
day_names = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}
print(f'Highest average departure delay: {day_names[max_day_dep_delay_name]} ({max_day_dep_delay:.2f} minutes).\n'
      f'Lowest average departure delay: {day_names[min_day_dep_delay_name]} ({min_day_dep_delay:.2f} minutes).')
# Overall cancellation rate
cancelled_flights = df['CANCELLED'].sum()
total_flights = len(df)
cancelled_percentage = cancelled_flights / total_flights
# Cancellation rate by carrier
total_carrier_flights = df['OP_UNIQUE_CARRIER'].value_counts()
carrier_cancelled_flights = df.groupby('OP_UNIQUE_CARRIER')['CANCELLED'].sum()
carrier_cancelled_rate = carrier_cancelled_flights / total_carrier_flights
min_carrier_cancelled = carrier_cancelled_rate.min()
min_carrier_name = carrier_cancelled_rate.idxmin()
max_carrier_cancelled = carrier_cancelled_rate.max()
max_carrier_name = carrier_cancelled_rate.idxmax()
print(f'Overall cancellation rate: {cancelled_percentage:.2%}\n'
      f'The carrier with the lowest cancellation rate is {min_carrier_name} ({min_carrier_cancelled:.2%}).\n'
      f'The carrier with the highest cancellation rate is {max_carrier_name} ({max_carrier_cancelled:.2%}).')
# Overall departure delay
avg_dep_delay = df['DEP_DELAY'].mean()
median_dep_delay = df['DEP_DELAY'].median()
print(f'Average departure delay: {avg_dep_delay:.2f} minutes\n'
      f'Median departure delay: {median_dep_delay:.2f} minutes')
# What percentage of flights had a departure delay greater than 15 minutes?
dep_delay = df['DEP_DELAY'].dropna()
dep_delayed = np.where(dep_delay > 15, 1, 0)
percentage_dep_delayed = dep_delayed.mean()
print(f'Percentage of flights with departure delay greater than 15 minutes: {percentage_dep_delayed:.2%}')
# Average departure delay by carrier
carrier_avg_dep_delay = df.groupby('OP_UNIQUE_CARRIER')['DEP_DELAY'].mean()
min_carrier_avg_dep_delay = carrier_avg_dep_delay.min()
min_dep_delay_name = carrier_avg_dep_delay.idxmin()
max_carrier_avg_dep_delay = carrier_avg_dep_delay.max()
max_dep_delay_name = carrier_avg_dep_delay.idxmax()
print(f'Highest average departure delay by carrier: {max_carrier_avg_dep_delay:.2f} minutes ({max_dep_delay_name}).\n'
      f'Lowest average departure delay by carrier: {min_carrier_avg_dep_delay:.2f} minutes ({min_dep_delay_name}).')
# Overall arrival delay
avg_arr_delay = df['ARR_DELAY'].mean()
median_arr_delay = df['ARR_DELAY'].median()
print(f'Average arrival delay: {avg_arr_delay:.2f} minutes\n'
      f'Median arrival delay: {median_arr_delay:.2f} minutes')
# What percentage of flights had an arrival delay greater than 15 minutes?
arr_delay = df['ARR_DELAY'].dropna(d)
arr_delayed = np.where(arr_delay > 15, 1, 0)
percentage_arr_delayed = arr_delayed.mean()
print(f'Percentage of flights with arrival delay greater than 15 minutes: {percentage_arr_delayed:.2%}')
# Average arrival delay by carrier
carrier_avg_arr_delay = df.groupby('OP_UNIQUE_CARRIER')['ARR_DELAY'].mean()
min_carrier_avg_arr_delay = carrier_avg_arr_delay.min()
min_arr_delay_name = carrier_avg_arr_delay.idxmin()
max_carrier_avg_arr_delay = carrier_avg_arr_delay.max()
max_arr_delay_name = carrier_avg_arr_delay.idxmax()
print(f'Highest average arrival delay by carrier: {max_carrier_avg_arr_delay:.2f} minutes ({max_arr_delay_name}).\n'
      f'Lowest average arrival delay by carrier: {min_carrier_avg_arr_delay:.2f} minutes ({min_arr_delay_name}).')
# Top 5 carriers
print(f'Top 5 carriers by flight count:\n{total_carrier_flights.head()}')
