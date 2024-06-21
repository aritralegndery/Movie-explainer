import os

def split_file_into_segments(file_path, words_per_segment=1024):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Split the content into words
    words = content.split()

    # Calculate the number of segments
    segment_length = words_per_segment

    # Split the words into segments
    segments = [' '.join(words[i:i+segment_length]) for i in range(0, len(words), segment_length)]

    # Create the directory if it doesn't exist
    directory_name = "John Wick"
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    # Save each segment into a separate file
    for i, segment in enumerate(segments):
        segment_file_path = os.path.join(directory_name, f"segment_{i+1}.txt")
        with open(segment_file_path, 'w') as segment_file:
            segment_file.write(segment)

    print(f"File has been split into {len(segments)} segments and saved in the '{directory_name}' directory.")

# Example usage
split_file_into_segments('/home/coder/app/formatted.txt')
