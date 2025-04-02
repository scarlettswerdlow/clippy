import unittest
from src.clippy.SplitLine import SplitLine

class TestSplitLine(unittest.TestCase):

    def test_get_title_author(self):
        raw_clipping = """Book Title (Author Name)
        - Your Highlight on page 45 | location 678-680 | Added on Thursday, January 1, 2023
        This is the highlighted text."""
        clipping = SplitLine(raw_clipping)
        self.assertEqual(clipping.get_title_author(), "Book Title (Author Name)")

    def test_get_page(self):
        raw_clipping = """Book Title (Author Name)
        - Your Highlight on page 45 | location 678-680 | Added on Thursday, January 1, 2023
        This is the highlighted text."""
        clipping = SplitLine(raw_clipping)
        self.assertEqual(clipping.get_page(), 45)

    def test_get_locations(self):
        raw_clipping = """Book Title (Author Name)
        - Your Highlight on page 45 | location 678-680 | Added on Thursday, January 1, 2023
        This is the highlighted text."""
        clipping = SplitLine(raw_clipping)
        self.assertEqual(clipping.get_locations(), (678, 680))

    def test_get_date_added(self):
        raw_clipping = """Book Title (Author Name)
        - Your Highlight on page 45 | location 678-680 | Added on Thursday, January 1, 2023
        This is the highlighted text."""
        clipping = SplitLine(raw_clipping)
        self.assertEqual(clipping.get_date_added(), "Thursday, January 1, 2023")

    def test_get_text(self):
        raw_clipping = """Book Title (Author Name)
        - Your Highlight on page 45 | location 678-680 | Added on Thursday, January 1, 2023
        This is the highlighted text."""
        clipping = SplitLine(raw_clipping)
        self.assertEqual(clipping.get_text(), "This is the highlighted text.")

    def test_empty_clipping(self):
        raw_clipping = ""
        clipping = SplitLine(raw_clipping)
        self.assertIsNone(clipping.get_title_author())
        self.assertIsNone(clipping.get_page())
        self.assertEqual(clipping.get_locations(), (None, None))
        self.assertIsNone(clipping.get_date_added())
        self.assertIsNone(clipping.get_text())

    def test_partial_clipping(self):
        raw_clipping = """Book Title (Author Name)
        - Your Highlight on Location 1047-1050 | Added on Tuesday, November 26, 2024 9:19:07 PM"""
        clipping = SplitLine(raw_clipping)
        self.assertEqual(clipping.get_title_author(), "Book Title (Author Name)")
        self.assertEqual(clipping.get_page(), None)
        self.assertEqual(clipping.get_locations(), (1047, 1050))
        self.assertEqual(clipping.get_date_added(), "Tuesday, November 26, 2024 9:19:07 PM")
        self.assertIsNone(clipping.get_text())

if __name__ == "__main__":
    unittest.main()