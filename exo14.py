# Word in a Frame

def print_word_in_frame():
    # Ask the user for a word
    word = input("Word: ").strip()

    # Define the width of the frame
    frame_width = 30

    # Calculate padding on each side
    total_padding = frame_width - len(word)
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding

    # Print the frame
    print("*" * frame_width)
    print("*" + " " * left_padding + word + " " * right_padding + "*")
    print("*" * frame_width)

# Run the program
print_word_in_frame()
