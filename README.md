# Codebase Method Finder

This script scans through every folder and file in a specified codebase, finds all references to specific methods, and stores the information in a CSV file. You can designate which methods to search for by updating the `methods_to_find` list with method names.

## Requirements

- Python 3.6 or higher
- pandas library
- A virtual environment (venv)

## Installation

1. Clone this repository to your local machine.
2. Navigate to the directory containing the script.
3. Set up a virtual environment:

```bash
python3 -m venv venv
```

4. Activate the virtual environment:

On Windows, run:
```bash
venv\Scripts\activate
```

On Unix or MacOS, run:
```bash
source venv/bin/activate
```

5. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the script from the command line, providing the starting directory as the first command line argument and a filename for the export csv as the second command line argument (do not include .csv in filename):

```bash
python script.py /path/to/directory file_name
```

Replace `/path/to/directory` with the directory you want to start traversing.

When it's done, it will create a CSV file named `filename.csv` in this directory. This file contains the following information for each method found:

- Name of the file where the method is referenced
- The method that was found
- The name of the method calling the found method
- The line number where the method is called
- The parent directory of the file
- An array of every file that references the calling method

## Note

This script assumes that the codebase is written in Ruby, as it looks for `.rb` files. If your codebase is written in a different language, you will need to modify the script accordingly.