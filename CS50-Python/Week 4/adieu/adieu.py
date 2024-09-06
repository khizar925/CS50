import sys

# Initialize an empty list to store names
names = []

# Read input from the user until EOF (control-d)
for line in sys.stdin:
    names.append(line.strip())

# Build the output string based on the number of names
if len(names) == 1:
    output = f"Adieu, adieu, to {names[0]}"
elif len(names) == 2:
    output = f"Adieu, adieu, to {names[0]} and {names[1]}"
else:
    output = f"Adieu, adieu, to {', '.join(names[:-1])}, and {names[-1]}"

# Print the final output
print(output)
