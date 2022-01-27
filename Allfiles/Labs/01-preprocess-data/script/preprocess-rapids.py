# import libraries
import os
import argparse

import cudf
import mlflow

# define functions

def main():

    # Set the columns and their datatypes for conversion and parsing
    cols = ['Flight_Number_Reporting_Airline', 'Year', 'Quarter', 'Month', 'DayOfWeek', 'DOT_ID_Reporting_Airline', 'OriginCityMarketID',  'DestCityMarketID', 'DepTime', 'DepDelay', 'DepDel15', 'ArrTime', 'ArrDelay', 'ArrDel15', 'CRSDepTime', 'CRSArrTime', 'AirTime', 'Distance', 'Reporting_Airline', 'IATA_CODE_Reporting_Airline', 'Origin', 'OriginCityName', 'Dest', 'DestCityName', 'Cancelled']

    dtypes = {'Flight_Number_Reporting_Airline': 'float32', 'Year': 'float32', 'Quarter': 'float32', 'Month': 'float32', 'DayOfWeek': 'float32', 'DOT_ID_Reporting_Airline': 'float32', 'OriginCityMarketID': 'float32', 'DestCityMarketID': 'float32', 'DepTime': 'float32', 'DepDelay': 'float32', 'DepDel15': 'int', 'ArrTime': 'float32', 'ArrDelay': 'float32', 'ArrDel15': 'int', 'CRSDepTime': 'float32', 'CRSArrTime': 'float32', 'AirTime': 'float32', 'Distance': 'float32', 'Reporting_Airline': 'str', 'IATA_CODE_Reporting_Airline': 'str', 'Origin': 'str', 'OriginCityName': 'str', 'Dest': 'str', 'DestCityName': 'str', 'Cancelled': 'str'}

    categorical_columns = ['Flight_Number_Reporting_Airline', 'DepTime', 'ArrTime', 'CRSDepTime', 'CRSArrTime', 'Reporting_Airline', 'Origin', 'OriginCityName', 'Dest', 'DestCityName', 'Airline']

    # Process the full dataset and save it to file
    processed_data = process_data(cols, dtypes, categorical_columns)
    
    count_rows = len(processed_data)
    mlflow.log_metric("processed rows", count_rows)

    processed_data.to_csv('outputs/processed_data.csv', index=False)
    
# Define a function to process an entire dataset 
def process_data(cols, dtypes, categorical_columns):        
    # Ingest - Read the CSV files into the DataFrame
    data = cudf.read_csv('./data/airlines_raw.csv', cols=cols, dtypes=dtypes)[cols] # Read in data, ignoring any column not in cols
    carriers = cudf.read_csv('./data/carriers.csv')
    airports = cudf.read_csv('./data/airports.csv', usecols=['iata_code', 'latitude_deg', 'longitude_deg',  'elevation_ft'])       
    
    # Merge - Combine the external data with the airline data         
    data = cudf.merge(data, carriers, left_on='IATA_CODE_Reporting_Airline', right_on='Code', how='left')
    data = cudf.merge(data, airports, left_on='Dest', right_on='iata_code', how='left')
    data = cudf.merge(data, airports, left_on='Origin', right_on='iata_code', how='left')            

    # Rename - Add clarity to the combined dataset by renaming columns
    data = data.rename(columns= { 'latitude_deg_x' : 'dest_lat', 'longitude_deg_x': 'dest_long',
                                  'latitude_deg_y' : 'origin_lat', 'longitude_deg_y': 'origin_long',
                                  'elevation_ft_x' : 'dest_elevation', 'elevation_ft_y' : 'origin_elevation',
                                  'Description' : 'Airline'})

    # Remove duplicates columns
    data = data.drop(['iata_code_x', 'iata_code_y','IATA_CODE_Reporting_Airline', 'Code'], axis=1)

    print(f'Added the following columns/features:\n { set(data.columns).difference(cols) }\n')
    print(f'Data currently has {data.shape[0]} rows and {data.shape[1]} columns\n')
    
    # Remove rows missing data
    data = data.dropna() 
    print(f'Dropping rows with missing or NA values, data now has {data.shape[0]} rows and {data.shape[1]} columns\n')
         
    # Encode - Convert human-readable names to corresponding computer-readable integers
    encodings, mappings = data['OriginCityName'].factorize() # encode/categorize a sample feature 
    print("Example encoding:")    
    numeric_columns = []
    for colname in data.columns:
        if colname in categorical_columns:
            values = data[colname].astype('category').cat.codes.astype('float32')
            colname = 'enc_' + colname                
            data.insert(0, colname, values)                
        numeric_columns += [colname]  
    print(list(zip(data['OriginCityName'][0:3].values_host, encodings[0:3])))

    # Remove redundant, surrogate, and unwanted columns from the data
    remove_cols = set (['Year', 'Cancelled', 'DOT_ID_Reporting_Airline', 'enc_IATA_CODE_Reporting_Airline', 'ArrTime']); 
    output_columns = list(set(numeric_columns).difference(remove_cols))

    # Add back additional columns that are used for data visualization, but not training
    output_columns = output_columns + ['OriginCityName', 'DestCityName']

    data = data[output_columns]
    print(f'Encoded and removed extra columns, data now has {data.shape[0]} rows and {data.shape[1]} columns\n')
    print(f'Removed: {remove_cols}')
    print(f'Returning: {output_columns}')

    return data

# run script
if __name__ == "__main__":
    # add space in logs
    print("\n\n")
    print("*" * 60)

    # run main function
    main()

    # add space in logs
    print("*" * 60)
    print("\n\n")

