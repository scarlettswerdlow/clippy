import re

class SplitLine:
    """
    A class to represent and parse a single Kindle clipping.

    This class takes a raw Kindle clipping as input and provides methods to extract
    structured information such as the title and author, page number, start and end
    locations, date added, and the highlighted text.

    Attributes:
        split_line (list): A list of non-empty lines from the raw Kindle clipping.

    Methods:
        get_title_author(): Returns the title and author of the clipping.
        get_page(): Returns the page number of the clipping, if available.
        get_locations(): Returns the start and end locations of the clipping.
        get_date_added(): Returns the date the clipping was added.
        get_text(): Returns the highlighted text from the clipping.
    """

    def __init__(self, raw_line):
        """
        Initialize the SplitLine object.

        :param raw_line: The raw Kindle clipping text
        :type raw_line: str
        """
        # Split the raw line into parts, removing empty strings
        self.split_line = [s.strip() for s in raw_line.split("\n") if s]

    def get_title_author(self):
        """
        Get title and author from the Kindle clipping.

        :return: Title and author as a string
        :rtype: str
        """
        return self.split_line[0] if len(self.split_line) > 0 else None

    def get_page(self):
        """
        Get the page number from the Kindle clipping.

        :return: Page number as an integer, or None if not available
        :rtype: int or None
        """
        if len(self.split_line) < 2:
            return None
        page_location_date = self.split_line[1].split("|")
        if len(page_location_date) == 2:
            return None
        try:
            page = re.search(r'\d+', page_location_date[0]).group()
            return int(page)
        except (IndexError, AttributeError):
            return None

    def get_locations(self):
        """
        Get the start and end locations from the Kindle clipping.

        :return: A tuple of (start_location, end_location)
        :rtype: tuple(int, int) or tuple(None, None)
        """
        if len(self.split_line) < 2:
            return None, None
        page_location_date = self.split_line[1].split("|")
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

    def get_date_added(self):
        """
        Get the date the clipping was added.

        :return: Date as a string, or None if not available
        :rtype: str or None
        """
        if len(self.split_line) < 2:
            return None
        page_location_date = self.split_line[1].split("|")
        try:
            date = page_location_date[-1]
            return date.strip(" Added on ").strip()
        except IndexError:
            return None

    def get_text(self):
        """
        Get the highlighted text from the Kindle clipping.

        :return: Highlighted text as a string, or None if not available
        :rtype: str or None
        """
        return self.split_line[2].strip() if len(self.split_line) > 2 else None