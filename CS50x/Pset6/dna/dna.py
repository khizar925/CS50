import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Error: filename.py {database_path} {Sequence}")
        sys.exit(1)
    database_path = sys.argv[1]
    sequence_path = sys.argv[2]

    # TODO: Read database_path file into a variable
    with open(database_path) as file:
        reader = csv.DictReader(file)
        # Assuming the first row contains column names and the first column is the word name
        fieldnames = reader.fieldnames
        rows = [row for row in reader]

    # TODO: Read DNA sequence file into a variable
    with open(sequence_path, 'r') as file1:
        sequence = file1.readline().strip()

    # TODO: Find longest match of each STR in DNA sequence
    matches = {}
    for field in fieldnames[1:]:
        longest_run = longest_match(sequence, field)
        matches[field] = longest_run

    # TODO: Check database_path for matching profiles
    for row in rows:
        if all(int(row[field]) == matches[field] for field in matches):
            print(row[fieldnames[0]])
            return

    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run


main()