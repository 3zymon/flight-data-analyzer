# Flight Data Analyzer
A small data analysis project exploring flight delays, cancellations, and carrier performance using real-world U.S. flight data.

## Project Goal
The goal of this project is to practice working with real-world datasets using Python, Pandas, and NumPy.
The analysis focuses on flight delays, cancellations, carrier performance, and data quality.

## Dataset
The dataset comes from the U.S. Bureau of Transportation Statistics (BTS) and contains flight-level data for January 2026.

The dataset contains 544,003 flight records and includes information about:
* flight dates
* operating carriers
* departure and arrival delays
* cancellations and diversions
* airports and routes
* flight distance
* air time

## Technologies
* Python
* Pandas
* NumPy

## Data Exploration
The analysis includes:
* initial dataset inspection
* data types and descriptive statistics
* missing value analysis
* duplicate record detection
* date conversion
* basic data cleaning
* day-of-week analysis

## Analysis
The project investigates questions such as:
* What is the average and median departure delay?
* What is the average and median arrival delay?
* Which days of the week have the highest average delays?
* Which carriers have the highest and lowest average delays?
* What percentage of flights are delayed by more than 15 minutes?
* What is the overall cancellation rate?
* Which carriers have the highest cancellation rates?
* Which carriers operate the most flights?

## Key Findings
Some results from the analysis:
* The overall cancellation rate was 2.82%.
* The average departure delay was 13.10 minutes, while the median was -2 minutes.
* The average arrival delay was 6.42 minutes, while the median was -7 minutes.
* 20.03% of flights had a departure delay greater than 15 minutes.
* 20.13% of flights had an arrival delay greater than 15 minutes.
* Monday had the highest average departure delay at 19.52 minutes.
* Wednesday had the lowest average departure delay at 8.19 minutes.
* AA had the highest average departure delay at 20.91 minutes.
* B6 had the highest average arrival delay at 16.09 minutes.
* WN operated the largest number of flights with 102,929 flights.

## Data Quality
The dataset contains missing values in several flight-operation fields.

Missing values were investigated in the context of:
* cancelled flights
* diverted flights
* missing departure delays
* missing arrival delays
* missing air time

Duplicate records were also investigated and removed before further analysis.

## Project Structure
```text
flight-data-analyzer/
├── data/
│   └── flights_2026_01.csv
├── analysis.py
├── README.md
└── .gitignore
```
## What I Practiced
This project helped me practice:

* working with real-world datasets
* Pandas DataFrame manipulation
* data cleaning
* missing value analysis
* grouping and aggregation
* statistical calculations with NumPy
* exploratory data analysis
* interpreting analytical results
