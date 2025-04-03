import unittest
import os
from src.clippy.Clipping import Clipping, Clippings

class TestClipping(unittest.TestCase):

    def test_title_author(self):
        raw_clipping = """Book Title (Author Name)
        - Your Highlight on page 45 | location 678-680 | Added on Thursday, January 1, 2023
        This is the highlighted text."""
        clipping = Clipping(raw_clipping)
        self.assertEqual(clipping.title_author, "Book Title (Author Name)")

    def test_page(self):
        raw_clipping = """Book Title (Author Name)
        - Your Highlight on page 45 | location 678-680 | Added on Thursday, January 1, 2023
        This is the highlighted text."""
        clipping = Clipping(raw_clipping)
        self.assertEqual(clipping.page, 45)

    def test_locations(self):
        raw_clipping = """Book Title (Author Name)
        - Your Highlight on page 45 | location 678-680 | Added on Thursday, January 1, 2023
        This is the highlighted text."""
        clipping = Clipping(raw_clipping)
        self.assertEqual(clipping.start_location, 678)
        self.assertEqual(clipping.end_location, 680)

    def test_date_added(self):
        raw_clipping = """Book Title (Author Name)
        - Your Highlight on page 45 | location 678-680 | Added on Thursday, January 1, 2023
        This is the highlighted text."""
        clipping = Clipping(raw_clipping)
        self.assertEqual(clipping.date, "Thursday, January 1, 2023")

    def test_text(self):
        raw_clipping = """Book Title (Author Name)
        - Your Highlight on page 45 | location 678-680 | Added on Thursday, January 1, 2023
        This is the highlighted text."""
        clipping = Clipping(raw_clipping)
        self.assertEqual(clipping.text, "This is the highlighted text.")

    def test_empty_clipping(self):
        raw_clipping = ""
        clipping = Clipping(raw_clipping)
        self.assertIsNone(clipping.title_author)
        self.assertIsNone(clipping.page)
        self.assertIsNone(clipping.start_location)
        self.assertIsNone(clipping.end_location)
        self.assertIsNone(clipping.date)
        self.assertIsNone(clipping.text)

    def test_partial_clipping(self):
        raw_clipping = """Book Title (Author Name)
        - Your Highlight on Location 1047-1050 | Added on Tuesday, November 26, 2024 9:19:07 PM"""
        clipping = Clipping(raw_clipping)
        self.assertEqual(clipping.title_author, "Book Title (Author Name)")
        self.assertIsNone(clipping.page)
        self.assertEqual(clipping.start_location, 1047)
        self.assertEqual(clipping.end_location, 1050)
        self.assertEqual(clipping.date, "Tuesday, November 26, 2024 9:19:07 PM")
        self.assertIsNone(clipping.text)

class TestClippings(unittest.TestCase):

    def test_add_clipping(self):
        clippings = Clippings()
        raw_clipping = """Book Title (Author Name)
        - Your Highlight on page 45 | location 678-680 | Added on Thursday, January 1, 2023
        This is the highlighted text."""
        clipping = Clipping(raw_clipping)
        clippings.add_clipping(clipping)
        self.assertEqual(len(clippings.clippings), 1)
        self.assertEqual(clippings.clippings[0].title_author, "Book Title (Author Name)")

    def test_save_to_csv(self):
        clippings = Clippings()
        raw_clipping_1 = """Book Title 1 (Author Name 1)
        - Your Highlight on page 10 | location 100-105 | Added on Monday, January 2, 2023
        This is the first highlighted text."""
        raw_clipping_2 = """Book Title 2 (Author Name 2)
        - Your Highlight on page 20 | location 200-205 | Added on Tuesday, January 3, 2023
        This is the second highlighted text."""

        # Add clippings
        clippings.add_clipping(Clipping(raw_clipping_1))
        clippings.add_clipping(Clipping(raw_clipping_2))

        # Save to CSV
        output_file_path = "test_clippings.csv"
        clippings.save_to_csv(output_file_path)

        # Verify the file exists
        self.assertTrue(os.path.exists(output_file_path))

        # Verify the contents of the file
        with open(output_file_path, "r", encoding="utf-8") as csvfile:
            lines = csvfile.readlines()
            self.assertEqual(len(lines), 3)  # Header + 2 clippings
            self.assertIn("Book Title 1 (Author Name 1)", lines[1])
            self.assertIn("Book Title 2 (Author Name 2)", lines[2])

        # Clean up
        os.remove(output_file_path)

if __name__ == "__main__":
    unittest.main()