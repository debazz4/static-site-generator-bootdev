import re

def count_hashes_at_beginning(input_string):
    # Use a regular expression to match consecutive '#' characters at the beginning of the string
    match = re.match(r'^#+', input_string)
    if match:
        return len(match.group(0))
    else:
        return 0

# Example usage
input_string = "### This is a heading"
num_hashes = count_hashes_at_beginning(input_string)
print("Number of '#' characters at the beginning:", num_hashes)

