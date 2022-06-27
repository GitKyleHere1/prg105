# A program that takes ciphertext from a file and converts it to plaintext to show on the terminal

# Def main
def main():
    # Get ciphertext file from user
    cipher_file = input("Please enter the cipher file to be decoded: ")

    # Try opening file for reading, if error, exit
    try:
        # Have to open and close cipher file, for some reason the editor flags ref error if we open it in try
        cipher_infile = open(cipher_file, "r")
        cipher_infile.close()

    except IOError:
        print("That file does not exist, please try again.")
        exit()

    # Open the file outside the try statement to avoid ref before assignment flag
    cipher_infile = open(cipher_file, "r")

    # Read from the ciphertext file and store as cipher_text
    ciphertext = cipher_infile.readlines()

    # Strip the newline characters from the ciphertext list
    for key, item in enumerate(ciphertext):
        ciphertext[key] = ciphertext[key].rstrip("\n")

    # Send ciphertext to decipher function to get the plaintext conversion
    plaintext = decipher(ciphertext)

    # Print the plaintext to the terminal
    print(plaintext)

    # Close the ciphertext file
    cipher_infile.close()


# Uses a key to convert plaintext to ciphertext
def decipher(ciphertext):
    plain = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=",
             "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "[", "]", "\\",
             "a", "s", "d", "f", "g", "h", "j", "k", "l", ";", "'",
             "z", "x", "c", "v", "b", "n", "m", ",", ".", "/",
             "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+",
             "{", "}", "|", ":", "\"", "<", ">", "?", " ",
             "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
             "A", "S", "D", "F", "G", "H", "J", "K", "L",
             "Z", "X", "C", "V", "B", "N", "M"]

    cipher_key = [" ", "a", "z", "w", "s", "x", "e", "d", "c", "r", "f", "v",
                  "t", "g", "b", "y", "h", "n", "j", "u", "m", "i", "k", ",", "o",
                  "l", ".", "p", ";", "/", "[", "'", "]", "\\", "1", "2",
                  "3", "4", "5", "6", "7", "8", "9", "0", "-", "=",
                  "+", "_", ")", "(", "*", "&", "^", "%", "$", "#", "@", "!",
                  "?", ">", "<", "\"", ":", "}", "{", "|", "q",
                  "P", "O", "I", "U", "Y", "T", "R", "E", "W", "Q",
                  "L", "K", "J", "H", "F", "G", "D", "S", "A",
                  "M", "N", "B", "C", "V", "X", "Z"]

    # Create empty string for plaintext
    plaintext = ""

    # Loop through each char in ciphertext and add the conversion to plaintext variable
    for char in ciphertext:
        plaintext += plain[cipher_key.index(char)]

    # Return the full plaintext string to main function
    return plaintext


# Call main
main()
