import pandas as pd

def transform(file_path):
    """
    Transforms the raw data into a pandas DataFrame.

    Args:
        file_path (str): Path to the raw data file.
    
    Returns:
        A pandas DataFrame containing the transformed data.
    """
    
    # Open text file
    with open(file_path, 'r') as f:
        lines = f.readlines()[31:]
    

    # Extract column names (now the first line of lines)
    column_names = [col.strip() for col in lines[0].lstrip('#').split(',')]
    
    # Convert each line of data to a list of values
    data = []
    
    for line in lines[2:]:
        values = [value.strip() for value in line.split(',')]
        data.append(values)
    
    # Load data into an pandas dataframe
    df = pd.DataFrame(data, columns=column_names)
    
    return df    
    

    

