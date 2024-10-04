README: City and Location Grouping Script
Overview
This Python script converts a .txt file containing city and location data into a JSON file, grouping cities based on their tier levels (e.g., Tier 1, Tier 2). Each tier will have a list of cities and their corresponding locations. The script processes the text file line by line, extracts the city name, location, and tier, and organizes the information into a structured JSON format.

How it Works
Input Format: The input file should contain city and location information, followed by a category and tier in parentheses.

Data Processing:

City and Location Extraction: The script separates the city name from the location and removes extra content in parentheses.
Tier Extraction: The script identifies the tier number (e.g., Tier 1, Tier 2) from the text.
Grouping: Cities and locations are grouped based on their tier. The output JSON will contain a list of cities and locations under each tier.
Output Format: The final output is a JSON file where the cities and locations are grouped by tier level.

Usage Instructions
Requirements: You need Python installed on your computer.

File Preparation: Prepare a .txt file with city and location data formatted correctly.

Script Setup: Modify the paths in the script to point to your input .txt file and the location where you want the JSON file to be saved.

Run the Script: Save the script as a .py file and run it using Python.

Output: After running the script, a JSON file with the grouped data will be created in the specified location.

Why Use This Script?
Automatic Grouping: This script simplifies the process of organizing cities by tier, saving time and effort.
Structured Output: The JSON format is easy to read and integrate with other applications.
Scalability: The script can handle large datasets and accurately group cities and locations by tier.