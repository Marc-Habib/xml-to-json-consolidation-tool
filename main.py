import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox
from data_consolidation import parse_xml_file, consolidate_data

# Default values for input and output paths, and data split percentages
DEFAULT_INPUT_FOLDER = "/path/to/default/input"
DEFAULT_OUTPUT_FOLDER = "/path/to/default/output"
DEFAULT_TEST_PERCENTAGE = 30
DEFAULT_TRAINING_PERCENTAGE = 70

def browse_input_folder():
    """Open a dialog to select the input folder and update the entry field."""
    folder_selected = filedialog.askdirectory()
    input_folder_entry.delete(0, tk.END)
    input_folder_entry.insert(0, folder_selected)

def browse_output_folder():
    """Open a dialog to select the output folder and update the entry field."""
    folder_selected = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, folder_selected)

def run_consolidation():
    """Run the data consolidation process and handle user inputs and errors."""
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()
    test_percentage = float(test_percentage_entry.get())
    training_percentage = float(training_percentage_entry.get())
    output_prefix = output_prefix_entry.get()

    # Validate user inputs
    if not input_folder or not output_folder or not output_prefix:
        messagebox.showerror("Input Error", "Please fill in all fields")
        return

    try:
        # Consolidate data
        consolidate_data(input_folder, output_folder, test_percentage, training_percentage, output_prefix)
        messagebox.showinfo("Success", "Data consolidation completed successfully")
        root.destroy()  # Close the Tkinter window upon success
    except Exception as e:
        # Display error message in case of exception
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("XML to JSON Consolidation Tool")

# Create and place the input folder label and entry
input_folder_label = tk.Label(root, text="Input Folder")
input_folder_label.grid(row=0, column=0, padx=10, pady=5)
input_folder_entry = tk.Entry(root, width=50)
input_folder_entry.grid(row=0, column=1, padx=10, pady=5)
input_folder_entry.insert(0, DEFAULT_INPUT_FOLDER)
browse_input_button = tk.Button(root, text="Browse", command=browse_input_folder)
browse_input_button.grid(row=0, column=2, padx=10, pady=5)

# Create and place the output folder label and entry
output_folder_label = tk.Label(root, text="Output Folder")
output_folder_label.grid(row=1, column=0, padx=10, pady=5)
output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.grid(row=1, column=1, padx=10, pady=5)
output_folder_entry.insert(0, DEFAULT_OUTPUT_FOLDER)
browse_output_button = tk.Button(root, text="Browse", command=browse_output_folder)
browse_output_button.grid(row=1, column=2, padx=10, pady=5)

# Create and place the test percentage label and entry
test_percentage_label = tk.Label(root, text="Test Percentage")
test_percentage_label.grid(row=2, column=0, padx=10, pady=5)
test_percentage_entry = tk.Entry(root, width=10)
test_percentage_entry.grid(row=2, column=1, padx=10, pady=5)
test_percentage_entry.insert(0, str(DEFAULT_TEST_PERCENTAGE))

# Create and place the training percentage label and entry
training_percentage_label = tk.Label(root, text="Training Percentage")
training_percentage_label.grid(row=3, column=0, padx=10, pady=5)
training_percentage_entry = tk.Entry(root, width=10)
training_percentage_entry.grid(row=3, column=1, padx=10, pady=5)
training_percentage_entry.insert(0, str(DEFAULT_TRAINING_PERCENTAGE))

# Create and place the output prefix label and entry
output_prefix_label = tk.Label(root, text="Output Prefix")
output_prefix_label.grid(row=4, column=0, padx=10, pady=5)
output_prefix_entry = tk.Entry(root, width=20)
output_prefix_entry.grid(row=4, column=1, padx=10, pady=5)

# Create and place the run button
run_button = tk.Button(root, text="Run Consolidation", command=run_consolidation)
run_button.grid(row=5, column=0, columnspan=3, pady=20)

# Start the Tkinter main loop
root.mainloop()
