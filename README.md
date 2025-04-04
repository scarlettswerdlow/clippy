# Clippy

Clippy is a Python package for parsing Kindle's `My Clippings.txt` file. It extracts useful information such as the title, author, page number, Kindle locations, date added, and highlighted text, making it easier to analyze and organize your Kindle highlights.

## Features

- Parse Kindle's `My Clippings.txt` file into structured data.
- Extract the following fields:
  - `title_author`: Title and author of the work the clipping is from.
  - `page`: Page number of the clipping (if available).
  - `start_location`: Starting Kindle location of the clipping.
  - `end_location`: Ending Kindle location of the clipping.
  - `date_added`: Date the clipping was added.
  - `text`: Highlighted text from the clipping.
- Supports handling empty or malformed clippings gracefully.
- Save parsed clippings to a CSV file.

## Requirements

- Python >= 3.10

## Installation

Clone the repository:
   ```bash
   git clone https://github.com/yourusername/clippy.git
   cd clippy
   ```

## Usage
### Programmatic Usage
You can use Clippy as a library in your Python code:
```python
from clippy.Clipping import Clipping, Clippings

# Parse a single clipping
raw_clipping = """Book Title (Author Name)
- Your Highlight on page 45 | location 678-680 | Added on Thursday, January 1, 2023
This is the highlighted text."""
clipping = Clipping(raw_clipping)
print(clipping.title_author)  # Output: Book Title (Author Name)
print(clipping.text)          # Output: This is the highlighted text.

# Parse multiple clippings and save to CSV
clippings = Clippings()
clippings.add_clipping(clipping)
clippings.save_to_csv("output.csv")
```

### Example Script
You can also create your own script to parse and save clippings. For example:
```python
from clippy.Clipping import Clipping, Clippings

# Load raw clippings from a file
with open("data/My Clippings.txt", "r", encoding="utf-8") as file:
    raw_clippings = file.read().split("==========")

# Parse clippings
clippings = Clippings()
for raw_clipping in raw_clippings:
    if raw_clipping.strip():  # Skip empty clippings
        clippings.add_clipping(Clipping(raw_clipping))

# Save to CSV
clippings.save_to_csv("data/My Parsed Clippings.csv")
print("Clippings saved to data/My Parsed Clippings.csv")
```

## Project Structure
```
clippy/
├── src/
│   └── clippy/
│       ├── __init__.py
│       ├── Clipping.py       # Contains the Clipping and Clippings classes
├── data/
│   └── My Clippings.txt      # Example input file
├── examples/
│   └── example.py            # Example usage of the library
├── tests/
│   └── test_clipping.py      # Unit tests for Clipping and Clippings classes
└── README.md                 # Project documentation
```

## License
This project is licensed under the MIT License.