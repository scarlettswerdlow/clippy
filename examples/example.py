"""Script to demonstrate the usage of the clippy package"""

import os
import sys

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from clippy.Clipping import Clipping, Clippings

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

    # Open raw clippings. Assumes default formating of Kindle My Clippings.txt file
    with open (input_file_path, "r", encoding="utf-8-sig") as file:
        content = file.read()
        raw_clippings = content.split("==========")

    clippings = Clippings()
    for c in raw_clippings:
        if c.strip() == "":
            continue
        clipping = Clipping(c)
        clippings.add_clipping(clipping)

    clippings.save_to_csv(output_file_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clippy.py <input_file_path> <output_file_path>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)
