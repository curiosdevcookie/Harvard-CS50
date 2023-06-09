import csv
import sys


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

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
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

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py DATABASE SEQUENCE")
    
    # TODO: Read database file into a variable
    database = open(sys.argv[1], "r")
    reader = csv.DictReader(database)
    
    temp_list = {}
    for row in reader:
        row_values = []
        for i in range(1, len(reader.fieldnames)):
            row_values.append(int(row[reader.fieldnames[i]]))
        temp_list[row["name"]] = row_values

    # TODO: Read DNA sequence file into a variable
    dna = open(sys.argv[2], "r")
    sequence = dna.read()

    # Find longest match of each STR in DNA sequence
    longest_runs = []
    for i in range(1, len(reader.fieldnames)):
        longest_runs.append(longest_match(sequence, reader.fieldnames[i]))

    # Compare longest runs to STR counts in database
    # print(f"temp_list: {temp_list}")
    # print(f"longest_runs: {longest_runs}")
    for name in temp_list:
        if temp_list[name] == longest_runs:
            print(name)
            break
    else:
        print("No match")

    database.close()
    dna.close()


main()

