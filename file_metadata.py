import requests
import zipfile
import os
import hashlib
from datetime import date
import pandas as pd
import shutil


def get_clean_string_list(input_filename):
    # Open the file and turn the contents into a list of space-delimited strings
    # Then clean it by removing newlines and any empty strings

    with open(input_filename) as f:
        read_string = f.read()

    read_string = read_string.strip()
    read_string_list = read_string.split(" ")

    if "" in read_string_list:
        read_string_list.remove("")

    # Apply the function str.strip() to every element in the list to remove newline chars
    read_string_list = list(map(str.strip, read_string_list))
    return read_string_list


def get_hash_memory_optimized_256(f_path):
    h = hashlib.sha256()
    with open(f_path, 'rb') as file:
        block = file.read(512)
        while block:
            h.update(block)
            block = file.read(512)

    return h.hexdigest()


today = date.today() # note this is outside the loop; only needs to happen once

# Store the example top row from the assessment prompt, to enable a quick check later
first_row_solution_df = pd.DataFrame(
    {'File_Name':"sample_file_0.txt",
    'Sha256_Hexdigest':"89abab31bc4c08205ea4190cac98deb0b9844da121acff9de93ea41adade8a75",
    'File_Size':371240, 'Word_Count':32025,
    'Unique_Word_Count':29449, 'Current_Date':today}, index=[0])

# Download the zip file from the repo URL

headers = {
    "Authorization" : 'token ghp_r5***',
    "Accept": 'application/vnd.github.v3+json'
}

url = "https://github.com/jimmyislive/sample-files/archive/refs/heads/master.zip"

r = requests.get(url, headers=headers)

if r.status_code == 200:
    with open('output.zip', 'wb') as fh:
        fh.write(r.content)
else:
    print(r.text)

# Unzip the file
with zipfile.ZipFile("output.zip", 'r') as zip_ref:
    zip_ref.extractall("output")

# Change working directory to the newly unzipped folder containing the downloaded files
os.chdir(r"output/sample-files-master")

# Create the list of filenames in the folder
sample_files_list = []
# Iterate directory
for file in os.listdir(os.getcwd()):
    # Check only text files
    if file.endswith('.txt'):
        sample_files_list.append(file)

# Initialize the pandas dataframe
interview_df = pd.DataFrame(
    columns=['File_Name','Sha256_Hexdigest','File_Size','Word_Count', 'Unique_Word_Count',
    "Current_Date", "Temp_Order_Number"], index=list(range(0, len(sample_files_list), 1)))

# Loop through the list of files and extract the info, adding a row to the df for each
for file_num in range(len(sample_files_list)):
    filename = sample_files_list[file_num]

    # Create a number label from splitting the filename string, for later re-ordering.
    # First split by "_"
    filename_split_once = filename.split("_")
    # Split again (last element only) by "." to remove the .txt file extension
    filename_split_twice = filename_split_once[-1].split(".")
    # The "true" order label comes from the first element of this second split
    filename_order_number = filename_split_twice[0]

    # Get hexdigest and file size
    hexdigest = get_hash_memory_optimized_256(filename)
    file_size = os.path.getsize(filename)

    # To get word counts, create a cleaned list of space-delimited strings
    clean_string_list = get_clean_string_list(filename)
    word_count = len(clean_string_list)
    # To get the unique word count, eliminate duplicates by converting list to set,
    # then just get the length of the set
    unique_word_count = len(set(clean_string_list))

    # For spot checks (optional), print first/last elements in the cleaned list:
    #print("The first element in the clean string list is:")
    #print(clean_string_list[0])
    #print("The last element in the clean string list is:")
    #print(clean_string_list[-1])

    # Finally, add the info to the df
    interview_df.iloc[file_num] = pd.Series(
        {'File_Name':filename, 'Sha256_Hexdigest':hexdigest, 'File_Size':file_size, 'Word_Count':word_count,
        'Unique_Word_Count':unique_word_count, 'Current_Date':today, "Temp_Order_Number":int(filename_order_number)})

print("Dataframe assembled!")

# Return to original root directory
os.chdir("..")
os.chdir("..")

# Export the unordered CSV for testing purposes (optional)
#interview_df.to_csv("interview_unordered.csv", header=False, index=False)

# Sort the rows of interview_df by 'Temp_Order_Number' column
interview_df_ordered = interview_df.sort_values(by = 'Temp_Order_Number')
# Reset the index
interview_df_ordered = interview_df_ordered.reset_index()
# Drop the unneeded columns
interview_df_ordered = interview_df_ordered.drop(columns=['index', 'Temp_Order_Number'])

print("Quick test - check if first row matches the example solution (True/False):")
# COPY the first row of the generated output to avoid altering the submission.
first_row_to_check = interview_df_ordered.iloc[[0]].copy()
# To prevent datatype inconsistencies, convert all values to strings
first_row_to_check = first_row_to_check.astype(str)
first_row_solution_df = first_row_solution_df.astype(str)
print(first_row_to_check.equals(first_row_solution_df))

# Export ordered df to CSV (create a specialized folder for it first, if necessary)
if os.path.isdir("deliverable") == False:
    os.mkdir("deliverable")
interview_df_ordered.to_csv(r"deliverable/interview.csv", header=False, index=False)

# Remove output.zip and the unzipped output folder (don't need them anymore)
os.remove('output.zip')
shutil.rmtree('output')