import tkinter as tk
from func_data_wrangling import get_reports, get_group_household_dict, get_contacts, generate_output_df
from func_gui_elements import ask_inputs, ask_save_location

def main():
    # Initialise the root window
    root = tk.Tk()
    root.withdraw()  # Hide the main root window

    try:
        # Create GUI and get the file and folder paths
        contacts_path, dict_path, reports_path = ask_inputs(root)
        
        # Read into dataframes
        contacts_df = get_contacts(contacts_path)
        dict_df = get_group_household_dict(dict_path)
        reports_df = get_reports(reports_path)

        # Join dataframes to create output 
        output_df = generate_output_df(reports_df, contacts_df, dict_df)
        
        # Save the DataFrame as an Excel file
        output_path = ask_save_location(root)
        output_df.to_excel(output_path, index=False)
        print(f'Data saved to: {output_path}')
    
    except Exception as e:
        print(f'An error occurred: {e}')

    # Close the root window
    root.destroy()

if __name__ == '__main__':
    main()