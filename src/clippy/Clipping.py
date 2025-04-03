import re
import csv

class Clipping:
    """
    A class to represent a single Kindle clipping.

    This class takes a raw Kindle clipping as input and provides attributes to store
    structured information such as the title and author, page number, start and end
    locations, date added, and the highlighted text.

    Attributes:
        title_author (str): The title and author of the clipping.
        page (int or None): The page number of the clipping, if available.
        start_location (int or None): The start location of the clipping, if available.
        end_location (int or None): The end location of the clipping, if available.
        date (str or None): The date the clipping was added, if available.
        text (str or None): The highlighted text from the clipping.
    """

    def __init__(self, raw_line):
        """
        Initialize the Clipping object by parsing the raw Kindle clipping.

        :param raw_line: The raw Kindle clipping text
        :type raw_line: str
        """
        # Split the raw line into parts, removing empty strings
        split_line = [s.strip() for s in raw_line.split("\n") if s]

        # Parse and set attributes
        self.title_author = self._get_title_author(split_line)
        self.page = self._get_page(split_line)
        self.start_location, self.end_location = self._get_locations(split_line)
        self.date = self._get_date_added(split_line)
        self.text = self._get_text(split_line)

    def _get_title_author(self, split_line):
        """
        Get title and author from the Kindle clipping.

        :param split_line: A list of non-empty lines from the raw clipping
        :type split_line: list
        :return: Title and author as a string
        :rtype: str
        """
        return split_line[0] if len(split_line) > 0 else None

    def _get_page(self, split_line):
        """
        Get the page number from the Kindle clipping.

        :param split_line: A list of non-empty lines from the raw clipping
        :type split_line: list
        :return: Page number as an integer, or None if not available
        :rtype: int or None
        """
        if len(split_line) < 2:
            return None
        page_location_date = split_line[1].split("|")
        if len(page_location_date) == 2:
            return None
        try:
            page = re.search(r'\d+', page_location_date[0]).group()
            return int(page)
        except (IndexError, AttributeError):
            return None

    def _get_locations(self, split_line):
        """
        Get the start and end locations from the Kindle clipping.

        :param split_line: A list of non-empty lines from the raw clipping
        :type split_line: list
        :return: A tuple of (start_location, end_location)
        :rtype: tuple(int, int) or tuple(None, None)
        """
        if len(split_line) < 2:
            return None, None
        page_location_date = split_line[1].split("|")
        if len(page_location_date) == 2:
            location = page_location_date[0]
        elif len(page_location_date) == 3:
            location = page_location_date[1]
        else:
            return None, None

        locations = re.findall(r'\d+', location)
        start_location = int(locations[0]) if len(locations) > 0 else None
        end_location = int(locations[1]) if len(locations) > 1 else None
        return start_location, end_location

    def _get_date_added(self, split_line):
        """
        Get the date the clipping was added.

        :param split_line: A list of non-empty lines from the raw clipping
        :type split_line: list
        :return: Date as a string, or None if not available
        :rtype: str or None
        """
        if len(split_line) < 2:
            return None
        page_location_date = split_line[1].split("|")
        try:
            date = page_location_date[-1]
            return date.strip(" Added on ").strip()
        except IndexError:
            return None

    def _get_text(self, split_line):
        """
        Get the highlighted text from the Kindle clipping.

        :param split_line: A list of non-empty lines from the raw clipping
        :type split_line: list
        :return: Highlighted text as a string, or None if not available
        :rtype: str or None
        """
        return split_line[2].strip() if len(split_line) > 2 else None

    def __repr__(self):
        """
        Return a string representation of the Clipping object.

        :return: A string representation of the Clipping object
        :rtype: str
        """
        return (
            f"Clipping(title_author={self.title_author}, page={self.page}, "
            f"start_location={self.start_location}, end_location={self.end_location}, "
            f"date={self.date}, text={self.text})"
        )

class Clippings:
    """
    A class to represent a collection of Clipping objects.

    This class provides functionality to store multiple Clipping objects
    and save them to a CSV file.

    Attributes:
        clippings (list): A list of Clipping objects.
    """

    def __init__(self):
        """
        Initialize an empty Clippings object.
        """
        self.clippings = []

    def add_clipping(self, clipping):
        """
        Add a Clipping object to the collection.

        :param clipping: A Clipping object to add
        :type clipping: Clipping
        """
        self.clippings.append(clipping)

    def save_to_csv(self, output_file_path):
        """
        Save the Clippings to a CSV file.

        :param output_file_path: The file path to save the CSV file
        :type output_file_path: str
        """
        # Define the header for the CSV file
        header = ["title_author", "page", "start_location", "end_location", "date", "text"]

        # Open the file and write the data
        with open(output_file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)  # Write the header row

            # Write each Clipping's data as a row
            for clipping in self.clippings:
                writer.writerow([
                    clipping.title_author,
                    clipping.page,
                    clipping.start_location,
                    clipping.end_location,
                    clipping.date,
                    clipping.text
                ])