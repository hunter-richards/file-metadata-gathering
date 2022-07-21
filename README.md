# File Metadata Gathering *

## Overview ##

The purpose of this project is to provide a program that accurately gathers metadata about online text files, generates a dataset called interview.csv to store the gathered metadata, and - by running in a docker container - makes the generation and access of the dataset easy to reproduce.

The project deliverable is a zip file containing all the files necessary to recreate the process:
*This README.md file
*file_metadata.py
*requirements.txt
*Dockerfile

## How to Build and Run the Container ##

1. Unzip the zip file. Extract the files to a brand new, dedicated folder and set that new folder as your working directory.
2. Build the container: docker build -t cs-hunter-richards-file-metadata:0.0.1 .
3. Run the container, and use a bind mount to save the csv file in your working directory.
 1. PowerShell: *docker run --name cs-hunter-richards-file-metadata --mount type=bind,source=$pwd,target=/app/deliverable cs-hunter-richards-file-metadata:0.0.1*
 2. Ubuntu: *docker run --name cs-hunter-richards-file-metadata --mount type=bind,source=$(pwd),target=/app/deliverable cs-hunter-richards-file-metadata:0.0.1*
4. View the contents of the dataset in your working directory: *cat interview.csv*
