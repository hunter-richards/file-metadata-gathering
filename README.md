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

## Discussion ##

This section contains some of my thoughts about the experience of completing this exercise, and ties those thoughts back into my feelings about good coding practices in general. It is not essential for the exercise submission; it is an optional read.

My general approach toward this assignment fit into a familiar pattern which I and many others often follow when tackling challenges like this one. First I made sure I understood what needed to be done, and then I mapped out how to get there by breaking the problem into a series of smaller, more practical pieces and resolving them one by one. One piece, for example, was the need to programmatically download the files. After I had completed that piece, I needed to extract the information from the files. Again starting small, I first developed the code to do this for one file and made sure the outcome was correct. After that, I could move on to doing the same for many files. And so on. What at first may have seemed complex began to get progressively simpler.

In addition to this general mindset, there are other practices which I find particularly helpful when programming. Early on, I write a ton of print statements so I can see as much as possible what is going on under the hood. Does the value of a particular variable look the way it should at this point in the script, and if not, why not? This allows me to catch problems early on, before they become bigger problems. Of course, I always clean up the print statements later when they are no longer needed and the product is more mature. Similarly, I like to get a good look at the raw data to get a solid understanding of its structure and content. This also helped me a great deal when investigating why my initial calculations were off; it turned out that the first file had a trailing space at the end and, in addition, newline characters were inflating the count of unique words. The strip() method came to the rescue.

I am also passionate about code readability. It has been said - in the Python style guide, for example - that code is read much more often than it is written. Software engineering is an art as well as a science, and there are certain practices that can greatly enhance the productive power of code by simply making it easier to understand. Upon finishing the development of the core functionality for this exercise, I went back to my code and cleaned it up while referring to the Python style guide for inspiration. What might seem like minor touches - such as ensuring consistency of double vs. single quotation marks, using upper-case variable names for constants, and writing cleanly-worded comments - can collectively add up to make an enormous difference in quality. Furthermore, it's honestly just a lot more fun and enjoyable to write clean code. 

## Extras ##
