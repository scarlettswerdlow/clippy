# clippy

Python command-line tool to parse Kindle My Clippings.txt file into CSV.

Output is a CSV file with the following columns:

- `title_author` Title and author of work clipping is from
- `page` Page clipping is from
- `start_location` Kindle location clipping starts on
- `end_location` Kindle location clipping ends on
- `date_added` Date clipping was added to My Clippings.txt
- `text` Text highlighted in clipping

## Dependencies

- Requires Python >= 3.10

## Usage

From the command line:

```
python3 src/clippy/clippy.py "data/My Clippings.txt" "data/My Parsed Clippings.csv"
```

## License

MIT