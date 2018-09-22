You want to encode a word using numbers, and you are using 2 matrices of size 5x5, A(letters, except Q) and B(numbers from 1 to 25):

For each letter of the alphabet, the corresponding value is a -> 1, b -> 2 and so on.

The word that must be encoded is evaluated from left to right by taking one character at a time, then identifying the position of that character in the A matrix and then retrieving the corresponding code for that position in the B matrix. In each such iteration, after the encoding is performed, the A matrix will undergo some permutational changes as it will be explained below.

For each iteration:
1. Encode the letter of the input word that corresponds to the current iteration. That is: take the position of the letter in A matrix, and then get the code for that position from B matrix.
2. Afterwards, take the line that contains the letter from the current iteration and rotate the line to the left.
3. Now take the column that contains the letter from the current iteration and rotate it upwards with one position.
4. For the next iteration, keep the modified A matrix obtained in the previous iteration.

Input: String

Output: array with the codes in a single line separated by spaces.

Example:
For "restart", the output is  17     5    17    17    20     1    11.