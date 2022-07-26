# File Metadata Gathering #

## Overview ##

The purpose of this project is to provide a program that accurately gathers metadata about online text files, generates a dataset called interview.csv to store the gathered metadata, and - by running in a docker container - makes the generation and access of the dataset easy to reproduce.

The project deliverable is a zip file containing all the files necessary to recreate the process:
* This README.md file
* file_metadata.py
* requirements.txt
* Dockerfile

## How to Build and Run the Container ##

1. Unzip the zip file. Extract the files to a brand new, dedicated folder and set that new folder as your working directory.
2. Build the container: *docker build -t cs-hunter-richards-file-metadata:0.0.1 .*
3. Run the container, and use a bind mount to save the csv file in your working directory.
    1. PowerShell: *docker run --name cs-hunter-richards-file-metadata --mount type=bind,source=$pwd,target=/app/deliverable cs-hunter-richards-file-metadata:0.0.1*
    2. Ubuntu: *docker run --name cs-hunter-richards-file-metadata --mount type=bind,source=$(pwd),target=/app/deliverable cs-hunter-richards-file-metadata:0.0.1*
4. View the contents of the dataset in your working directory: *cat interview.csv*

## Summary of the Code ##

This section provides a brief summary of how the Python code generates the output CSV file.

First, the script downloads all of the .txt files in a single zip file from the URL. It unzips the file and creates a list of all the file names in the unzipped folder with the .txt extension. It then creates a pandas dataframe with the appropriate column names and a number of rows equal to the length of the .txt file name list. Looping through the list of .txt file names, the script retrieves the required information for each file and inserts the information as a row in the dataframe. It orders the dataframe in a more appropriate order (by extracting the number label from each file name) and exports to CSV.
