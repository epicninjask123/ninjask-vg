"""
17 August, 2018
Converts a .csv file to a list of Python dictionary objects.
Saves the result to a .py file which can be copy-pasted or imported.

This was written because vgcollect.com has an option to export my collection's
data, including all the games and their consoles, but it does so to a .csv
file. For developing, I'd like this to be processed via a python script,
which is why I'm converting it to a dictionary object.

The .csv file should contain all of the keys on the first line.
Each subsequent line is a new item with values corresponding to those keys.

To run, either import this into another script and call convert() with
"""

import argparse
import csv

# filename = the .csv file you want to convert
def convert(filename):
  try :
    with open(filename) as csv_file:
      csv_reader = csv.DictReader(csv_file)
      #csv_reader = csv.reader(csv_file, delimiter=',')
      for row in csv_reader:
        print(row)
        print(type(row))
        print()
      
  except Exception:
    print("An error has occurred. Please try again.")
  return

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='')
  parser.add_argument('fname')
  args = parser.parse_args()
  convert(args.fname)