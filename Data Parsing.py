import csv
import json
import xml.etree.ElementTree as ET
import sys
import os

# Check if the correct number of command-line arguments are provided
if len(sys.argv) != 2:
    print("Current working directory:", os.getcwd())
    #print("Usage: python script.py <output_format>")
    sys.exit(1)

# Update the input file name to 'data.txt'
input_file_path = 'C:/Users/Christian/OneDrive/Documents/Data Parsing/data.txt'
output_format = sys.argv[1]

#list to store JSON data
data = []

# Check the specified output format
if output_format == '-c':
    # Convert to CSV
    with open(input_file_path, 'r') as text_file:
        lines = text_file.readlines()
    with open('data.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='\t')  # Use tab as the delimiter
        for line in lines:
            # Split the line into fields using tabs as the delimiter
            record = line.strip().split('\t')
            csv_writer.writerow(record)

elif output_format == '-j':
    # Convert to JSON
    with open(input_file_path, 'r') as text_file:
        # Skip the header line
        header = next(text_file)
        for line in text_file:
            # Split the line into fields using tabs as the delimiter
            fields = line.strip().split('\t')
            record = {}
            # Create a dictionary with field names as keys and values from the line
            for i, field in enumerate(fields):
                header_field = header.strip().split('\t')[i]
                record[header_field] = field
            data.append(record)

    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)


elif output_format == '-x':
    # Convert to XML
    root = ET.Element('data')
    with open(input_file_path, 'r') as text_file:
        for line in text_file:
            # Assuming each line is a record to be converted to XML
            record = ET.SubElement(root, 'record')
            record.text = line.strip()
    tree = ET.ElementTree(root)
    tree.write('data.xml', encoding='utf-8')

else:
    print("Invalid output format. Use -c for CSV, -j for JSON, or -x for XML.")
    sys.exit(1)
