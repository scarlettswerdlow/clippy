# clippy

Library to parse Kindle My Clippings.txt file into CSV.

Output in a CSV file with the following columns:

- `title_author` Title and author of work clipping is from
- `page` Page clipping is from
- `start_location` Kindle location clipping starts on
- `end_location` Kindle location clipping ends on
- `date_added` Date clipping was added to My Clippings.txt
- `text` Text highlighted in clipping

## Usage

`python3 src/clippy/clippy.py "data/My Clippings.txt" "data/My Parsed Clippings.csv"`

## License

MIT License