import os
import re
import sys
import time
import pandas as pd

# List of methods to find
methods_to_find = ['upload_file_from_param_to_s3', 'upload_file_from_url_to_s3', 'upload_file_from_url_to_s3', 
                   'upload_local_file_to_s3', 'archive_file_to_s3', 'archive_file_to_s3', 'download_file_from_s3',
                   'get_s3_public_url', 'get_s3_url']

# Initialize an empty DataFrame
df = pd.DataFrame(columns=['File Name', 'Method Found', 'Line Number', 'Parent Directory'])

# Get the starting directory from the command line
if len(sys.argv) > 1:
    start_dir = sys.argv[1]
else:
    print("Please provide the starting directory as a command line argument.")
    sys.exit()

def progress_bar(total):
    # Initialize the progress
    progress = 0

    while progress <= total:
        # Calculate the percentage of completion
        percent_complete = (progress / total) * 100

        # Create the progress bar
        bar = '=' * int(percent_complete / 2)  # Each '=' represents 2% of the progress

        # Print the progress bar with the percentage
        sys.stdout.write("\r[%-50s] %d%%" % (bar, percent_complete))
        sys.stdout.flush()

        progress += 1
        yield

        # Simulate a delay
        time.sleep(0.1)

    print()

def determine_search_length(dir_path, file_type):
    # Does an initial scan of the directory and counts the number
    # of directories and files it will search
    dir_length = 0
    file_length = 0
    for root, dirs, files in os.walk(dir_path):
        dir_length += 1
        for file in files:
            if file.endswith(file_type):
                file_length += 1

    return (dir_length, file_length)

num_dir, num_files = determine_search_length(start_dir, '.rb')

# Traverse the file system
results = []
files_searched = 0
for root, dirs, files in os.walk(start_dir):
    tmp_dict = {}
    for file in files:
        files_searched += 1
        if file.endswith('.rb'):  # Assuming we are looking for Python files
            with open(os.path.join(root, file), 'r') as f:
                lines = f.readlines()
                for i, line in enumerate(lines):
                    for method in methods_to_find:
                        # Store the information in the DataFrame
                        tmp_dict['File Name'] = file
                        tmp_dict['Method Found'] = method
                        tmp_dict['Line Number'] = i + 1
                        tmp_dict['Parent Directory'] = root
                        results.append(tmp_dict)
                        tmp_dict = {}


# Add the results to the DataFrame
df = pd.concat([df, pd.DataFrame(results)], ignore_index=True)


# Create a CSV of the DataFrame
df.to_csv('method_references_s3.csv', index=False)
print(f'Files Searched: {files_searched}')