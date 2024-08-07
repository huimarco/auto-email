import os
import pandas as pd

# Function to get a list of all filenames of a given folder
def get_filenames(folder,file_type):
    # Get all files in the folder
    all_files = os.listdir(folder)

    # Filter for specified file type
    pdf_files = [f for f in all_files if f.endswith(file_type)]

    # Create a DataFrame from the list of files
    df = pd.DataFrame(pdf_files, columns=['filename'])

    return df

def get_reports(folderpath):
    # Load into dataframe
    df = get_filenames(folderpath, '.pdf')

    # Remove filename suffix to get portfolio column
    df['portfolio'] = df['filename'].str.split().str[:-1].str.join(' ')

    return df

def get_group_household_dict(filepath):
    # Load into dataframe
    df = pd.read_excel(filepath, sheet_name='dict')

    # Drop extra columns
    df.drop(columns=['combination'], inplace=True)

    return df

def get_contacts(filepath):
    # Load into dataframe
    df = pd.read_excel(filepath)

    # Rename columns
    df.columns = ['cpu_contact', 'cpu_checksum', 'cpu_modified', 
                  'full_name', 'first_name', 'middle_name', 'last_name', 'household', 'primary_advisor', 
                  'email', 'home_phone', 'mobile_phone', 'business_phone']
    
    # Filter out rows without email addresses
    df.dropna(subset=['email'], inplace=True)

    # Create a helper column for the position of each value in column 'email'
    df['email_position'] = df.groupby('household').cumcount() + 1

    # Pivot the DataFrame
    nodup_df = df.pivot_table(index='household', columns='email_position', values='email', aggfunc='first').reset_index()

    # Rename columns
    nodup_df.columns.name = None
    nodup_df.columns = ['household'] + [f'email_{i}' for i in nodup_df.columns[1:]]

    return nodup_df

def generate_output_df(reports_df, contacts_df, dict_df):
    # Adding the household column to reports_df
    temp_df = pd.merge(reports_df, dict_df, on='portfolio', how='left')

    # Create a new column that is True if the value in 'portfolio' is a duplicate
    temp_df['duplicate'] = temp_df['portfolio'].duplicated(keep=False)
    
    # Drop duplicates
    temp_nodup_df = temp_df.drop_duplicates(subset=['portfolio'], keep='first')

    # Add email columns to joined df
    result_df = pd.merge(temp_nodup_df, contacts_df, on='household', how='left')

    return result_df
