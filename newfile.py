# Define the prefixes to look for
prefixes = ['Text1', 'Text2']

# Open the input file and the output file
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    # Process each line in the input file
    for line in infile:
        # Check if the line starts with any of the prefixes
        if any(line.startswith(prefix) for prefix in prefixes):
            # Write the line to the output file
            outfile.write(line)
