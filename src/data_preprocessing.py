import pandas as pd
import numpy as np


# Define a function for the data preprocessing
def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    
    # List of columns to drop (corrected for exact names)
    col_to_drop = [
        'OBJECTID', 'SRC_AGENCY', 'FIRE_ID', 'FIRENAME', 'DAY', 'REP_DATE', 'ATTK_DATE', 
        'OUT_DATE', 'DECADE', 'CAUSE', 'PROTZONE', 'FIRE_TYPE', 'MORE_INFO', 'CFS_REF_ID', 
        'CFS_NOTE1', 'CFS_NOTE2', 'ACQ_DATE', 'SRC_AGY2', 'ECOZONE', 
        'ECOZ_REF', 'ECOZ_NAME', 'ECOZ_NOM'
    ]
    
    # Drop the columns
    df = df.drop(columns=col_to_drop, axis=1)
    df['LULC2'] = df['LULC2'].replace(11, 5)
    df['LULC2'] = df['LULC2'].replace(0, 3)
    
    replace_values_LULC = {
        1: 'Urban_areas',
        2: 'Crop_land',
        3: 'Grass_land',
        4: 'Tree_covered',
        5: 'Shrub_covered',
        6: 'Herbaceous',
        8: 'Sparse_vegetation',
        9: 'Bare_soil',
        10: 'Snow',
        11: 'Water_bodies'
    }
    
    df['LULC2'] = df['LULC2'].replace(replace_values_LULC)
    
    # List of new column names
    new_col_name = [
        'Latitude', 'Longitude', 'Year', 'Month', 'Size_ha', 'TWI', 'Temp_july',
        'Slope', 'Aspect', 'LULC', 'NDVI', 'Precipitation', 'SoilMoisture',
        'Elevation', 'Dist_Lakes', 'Dist_Roads', 'Dist_Rivers'
    ]
    
    # Assign the new column names
    df.columns = new_col_name
    
    # Dictionary mapping columns to their new data types
    data_types = {
        'Latitude': float,
        'Longitude': float,
        'Year': int,
        'Month': int,
        'Size_ha': float,
        'TWI': float,
        'Temp_july': float,
        'Slope': float,
        'Aspect': float,
        'LULC': 'category',
        'NDVI': float,
        'Precipitation': float,
        'SoilMoisture': float,
        'Elevation': float,
        'Dist_Lakes': float,
        'Dist_Roads': float,
        'Dist_Rivers': float
    }
    
    # Change the data types of the columns
    df = df.astype(data_types)
    
    return df

# Example usage
if __name__ == "__main__":
    processed_df = preprocess_data('Export_Raw10_ha.csv')
    print(processed_df.head())
