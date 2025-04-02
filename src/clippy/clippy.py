"""Module to parse Kindle My Clippings.txt file into CSV"""

import os
import sys
import csv
from SplitLine import SplitLine

def parse_line(line):
    """
    Parse Kindle clipping

    :param line: Clipping
    :type line: String
    """
    clipping = SplitLine(line)
    title_author = clipping.get_title_author()
    page = clipping.get_page()
    start_location, end_location = clipping.get_locations()
    date_added = clipping.get_date_added()
    text = clipping.get_text()
    return [title_author, page, start_location, end_location, date_added, text]

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
