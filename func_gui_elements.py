# Import libaries
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

# Function that asks user for output file location
def ask_save_location(root):
    result = filedialog.asksaveasfilename(parent=root, title='Save as', filetypes=[('Excel files', '*.xlsx')], defaultextension='.xlsx')
    if not result:  # Check if result is an empty string
        raise ValueError("Output file save location not provided. Exiting.")
    return result

def ask_inputs(root):
    inputs_window = tk.Toplevel(root)
    inputs_window.title('Select Files and Folder')

    # Variables to store file and folder paths
    contacts_path = tk.StringVar()
    dict_path = tk.StringVar()
    reports_path = tk.StringVar()

    def browse_contacts_file():
        # Browse and select the contact file
        contacts_path.set(filedialog.askopenfilename(title='Select Contacts Bulk Report File'))

    def browse_dict_file():
        # Browse and select the dictionary file
        dict_path.set(filedialog.askopenfilename(title='Select Group-Household Dictionary File'))

    def browse_report_folder():
        # Browse and select a folder
        reports_path.set(filedialog.askdirectory(title='Select Quarterly Reports Folder'))

    def submit():
        # Get the paths from the entry fields
        contacts = contacts_path.get()
        dict = dict_path.get()
        report = reports_path.get()

        # Check if all fields are filled
        if not contacts or not dict or not report:
            messagebox.showerror('Error', 'Please populate all fields.')
        else:
            print(f'Contacts File: {contacts}\nDict File: {dict}\nReports Folder: {report}')
            inputs_window.destroy()

    # Create and place the GUI components
    tk.Label(inputs_window, text='Contacts File:').grid(row=0, column=0, padx=10, pady=5)
    tk.Entry(inputs_window, textvariable=contacts_path, width=50).grid(row=0, column=1, padx=10, pady=5)
    tk.Button(inputs_window, text='Browse', command=browse_contacts_file).grid(row=0, column=2, padx=10, pady=5)

    tk.Label(inputs_window, text='Dictionary File:').grid(row=1, column=0, padx=10, pady=5)
    tk.Entry(inputs_window, textvariable=dict_path, width=50).grid(row=1, column=1, padx=10, pady=5)
    tk.Button(inputs_window, text='Browse', command=browse_dict_file).grid(row=1, column=2, padx=10, pady=5)

    tk.Label(inputs_window, text='Reports Folder:').grid(row=2, column=0, padx=10, pady=5)
    tk.Entry(inputs_window, textvariable=reports_path, width=50).grid(row=2, column=1, padx=10, pady=5)
    tk.Button(inputs_window, text='Browse', command=browse_report_folder).grid(row=2, column=2, padx=10, pady=5)

    tk.Button(inputs_window, text='Submit', command=submit).grid(row=3, column=1, pady=10)

    inputs_window.wait_window()  # Wait until the window is destroyed
    return contacts_path.get(), dict_path.get(), reports_path.get()