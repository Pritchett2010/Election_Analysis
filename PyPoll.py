# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular votes
# Create a filename variable to a direct or indirect path to the file
import os


file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file. 
open(file_to_save, "w")

# Create a file name variable to a direct or indirect path to the new file 
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file 
outfile.close()
# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

# Write some data to file.
    txt_file.write("Hello World")
    


