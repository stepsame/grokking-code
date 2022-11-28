"""
Decrypt Message
Every word is encrypted as follows:
  - Convert every letter to its ASCII value.
  - Add 1 to the first letter, and then for every letter from the second one to the last one, add the value of the previous letter.
  - Subtract 26 from every letter until it is in the range of lowercase letters a-z in ASCII.
  - Convert the values back to letters.
For instance, to encrypt the word “crime”
Decrypted message:  c   r   i   m   e
Step 1:             99  114 105 109 101
Step 2:            100  214 319 428 529
Step 3:            100  110 111 116 113
Encrypted message:  d   n   o   t   q
Write a function named decrypt(word) that receives a string that consists of small latin letters only, and returns the decrypted word.
input:  word = "dnotq"
output: "crime"
input:  word = "flgxswdliefy"
output: "encyclopedia"
"""

"""
Solution:
First of all, notice that the first letter is very easy to decrypt:
1.Convert the first letter back to its ASCII value.
2.Subtract 1 from it.
3.Move the value to be in the range of a-z ASCII values (97-122), by adding 26.
4.Convert the result back to a character.

The decryption of the rest of the letters is done by almost the same algorithm -
given the decrypted previous letter prev, and its value after the second step of encryption - denoted secondStepPrev:
1.Convert the current letter back to its ASCII value.
2.Subtract secondStepPrev from it.
3.Move the value to be in the range of a-z ASCII value (97-122), by adding multiples of 26.
4.Convert the result back to a character. Store its ASCII value in prev, and add its value to secondStepPrev (for the decryption of the next letter).

Time Complexity:
the function’s asymptotic time complexity is O(N), where N is the length of the input string.
 the loop that iterates through the letters in the input is performed N times.

Space Complexity: the space usage is also O(N) since the output is the same size of the input,
 and we only keep the output and the second step in storage.

"""


def solution(word):
    decryption = ""
    prev_letter_value = 1

    for letter in word:
        letter_ascii_value = ord(letter)
        letter_ascii_value -= prev_letter_value

        while letter_ascii_value < ord('a'):
            letter_ascii_value += 26

        decryption += chr(letter_ascii_value)
        prev_letter_value += letter_ascii_value
    print(decryption)
    return decryption


def main():
    assert solution(word = "dnotq") == "crime"
    assert solution(word = "flgxswdliefy") == "encyclopedia"


if __name__ == '__main__':
    main()
