"""
This script generates a sequence of pseudo-random bits (0s and 1s) and saves them to a text file.

Capabilities: Its core capability is to create a long, pseudo-random sequence of binary digits (0s and 1s) and save that sequence to a text file.

1. Generation: It uses Python's built-in 'random' module, which implements the Mersenne Twister algorithm, 
 suitable for non-cryptographic purposes.
2. Input/Output: It takes the generated 10,000-character string and writes it directly to a file named 
 rand_bits.txt, making the data immediately available for analysis or use by other applications.

"""

import random
import os

# Configuration: This constant defines how many bits we want to generate. It can be adjusted as needed.
BIT_COUNT = 10000 # Total number of bits to generate
BITS_PER_LINE = 100  # For formatting the output file
OUTPUT_FILENAME = "rand_bits.txt" # Output file name

def generate_random_bit_sequence(count): # Generate a sequence of random bits (0s and 1s)
   
    print(f"Generating {count} pseudo-random bits...")

    bit_sequence = "".join(random.choice(['0', '1']) for _ in range(count)) # randomly choose '0' or '1'
    
    return bit_sequence

def save_to_file(sequence, filename, line_length): # Save the bit sequence to a text file with specified line length
    
    if len(sequence) % line_length != 0:
        print("Warning: Total bit count is not perfectly divisible by the line length.")

    chunked_lines = [
        sequence[i:i + line_length] # Split the sequence into lines of specified length
        for i in range(0, len(sequence), line_length) # Create chunks of the specified line length
    ]
    try:
        with open(filename, 'w') as f:
            f.write("\n".join(chunked_lines))
        print(f"Thank you for using RANDBITGEN... Successfully saved {len(sequence)} bits to '{filename}' in the current directory.")
        print(f"Please Note: File contains {len(chunked_lines)} lines of {line_length} bits each.")

        print(f"\nHere is your sameple output (first 2 lines):\n") # Print a small sample for confirmation
        for i, line in enumerate(chunked_lines[:2], start=1):
            print(f"Line {i}: {line}")
        print("End of sample output.")
        print("\n...")
    
    except IOError as e:
        print(f"Error writing to file {filename}: {e}")

if __name__ == "__main__":
    
    sequence = generate_random_bit_sequence(BIT_COUNT) # Generate the random bit sequence
    
    save_to_file(sequence, OUTPUT_FILENAME, BITS_PER_LINE) # Save the sequence to a file
