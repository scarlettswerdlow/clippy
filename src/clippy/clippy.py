"""Module to parse Kindle My Clippings.txt file into CSV"""

import os
import sys
import re
import csv

def get_title_author(split_line):
    """
    Get title and author from Kindle clipping

    :param split_line: Clipping split on linebreak
    :type split_line: String
    """
    return split_line[0].strip()

def get_page(split_line):
    """
    Get page from Kindle clipping
    
    :param split_line: Clipping split on linebreak
    :type split_line: String
    """
    page_location_date = split_line[1].split("|")
    # Length of 2 means Kindle text does not have pages, only Kindle locations
    if len(page_location_date) == 2:
        return None
    try:
        page = re.search(r'\d+', page_location_date[0]).group()
        return int(page)
    except IndexError as e:
        print(f"Error {e} on line {split_line}")
        return None

def get_start_location(location):
    """
    Get Kindle start location from Kindle clipping
    
    :param location: Clipping split on linebreak and then split on |
    :type location: String
    """
    locations = re.findall(r'\d+', location)
    start_location = locations[0]
    return int(start_location)

def get_end_location(location):
    """
    Get Kindle end location from Kindle clipping
    
    :param location: Clipping split on linebreak and then split on |
    :type location: String
    """
    locations = re.findall(r'\d+', location)
    # Length of 1 means Kindle clipping only has starting location
    if len(locations) == 1:
        return None
    end_location = locations[1]
    return int(end_location)

def get_locations(split_line):
    """
    Get Kindle location from Kindle clipping
    
    :param split_line: Clipping split on linebreak
    :type split_line: String
    """
    page_location_date = split_line[1].split("|")
    # Length of 2 means Kindle text does not have pages, only Kindle locations
    if len(page_location_date) == 2:
        location = page_location_date[0]
        start_location = get_start_location(location)
        end_location = get_end_location(location)
    # Length of 3 means Kindle text has pages and locations
    if len(page_location_date) == 3:
        location = page_location_date[1]
        start_location = get_start_location(location)
        end_location = get_end_location(location)
    else:
        start_location = end_location = None
    return start_location, end_location

def get_date_added(split_line):
    """
    Get date clipping was made from Kindle clipping
    
    :param split_line: Clipping split on linebreak
    :type split_line: String
    """
    page_location_date = split_line[1].split("|")
    try:
        # Date is always last item on this line
        date = page_location_date[-1]
        return date.strip(" Added on ").strip()
    except IndexError as e:
        print(f"Error {e} on line {split_line}")
        return None

def get_text(split_line):
    """
    Get highlighted text from Kindle clipping
    
    :param split_line: Clipping split on linebreak
    :type split_line: String
    """
    try:
        text = split_line[2]
        return text.strip()
    except IndexError as e:
        print(f"Error {e} on line {split_line}")
        return None

def parse_line(line):
    """
    Parse Kindle clipping

    :param line: Clipping
    :type line: String
    """
    # Remove any empty strings from split line
    line_split = [s for s in line.split("\n") if s]
    title_author = get_title_author(line_split)
    page = get_page(line_split)
    location_start, location_end = get_locations(line_split)
    date_added = get_date_added(line_split)
    text = get_text(line_split)
    return [title_author, page, location_start, location_end, date_added, text]

def main(input_file_path, output_file_path):
    """
    Parse Kindle My Clippings.txt file into CSV

    :param input_file_path: File path to My Clippings.txt
    :type input_file_path: String
    :param output_file_path: File path to save parsed csv file
    :type output_file_path: String
    """
    # Check that file exists
    if not os.path.exists(input_file_path):
        print(f"Error: The file '{input_file_path}' does not exist.")
        sys.exit(1)

    # Check that file is not empty
    if os.path.getsize(input_file_path) == 0:
        print(f"Error: The file '{input_file_path}' is empty.")
        sys.exit(1)

    with open (input_file_path, "r", encoding="utf-8-sig") as file:
        content = file.read()
        lines = content.split("==========")

    clippings = [["title_author", "page", "start_location", "end_location", "date_added", "text"]]
    for line in lines:
        if line.strip() == "":
            continue
        parsed_line = parse_line(line)
        clippings.append(parsed_line)

    with open(output_file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(clippings)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clippy.py <input_file_path> <output_file_path>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
