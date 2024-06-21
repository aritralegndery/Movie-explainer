import re

with open('transcript.txt', 'r') as f:
    text = f.read()

# Replace all newline characters with spaces and then reduce multiple spaces to a single space
one_line_text = re.sub(r'\s+', ' ', text.replace("\n", " ")).strip()

# Print the length of the one-line text
print(len(one_line_text))

# Write the one-line text to a new file
with open('formatted.txt', 'w') as f:
    f.write(one_line_text)
