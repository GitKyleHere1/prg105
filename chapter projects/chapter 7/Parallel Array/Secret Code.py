# A program that takes plaintext and converts it to ciphertext and writes it to a file

# Def main
def main():
    # Get plaintext from user
    plaintext = input("Please enter a phrase to be converted to ciphertext:\n")

    # Send plaintext to cipher function to get the ciphertext conversion
    ciphertext = cipher(plaintext)

    # Open ciphertext file
    cipher_outfile = open("ciphertext.txt", "w")

    # Write to the ciphertext file
    cipher_outfile.writelines(ciphertext)

    # Close the ciphertext file
    cipher_outfile.close()


# Uses a key to convert plaintext to ciphertext
def cipher(plaintext):
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

    # Create empty string for ciphertext
    ciphertext = ""

    # Loop through each char in plaintext and add the conversion to ciphertext variable
    for char in plaintext:
        ciphertext += cipher_key[plain.index(char)] + "\n"

    # Return the full ciphertext string to main function
    return ciphertext


# Call main
main()
