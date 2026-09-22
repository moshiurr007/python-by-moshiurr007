## Number Guessing Game

### Challenge

Build a number guessing game. The computer picks a random integer between 1 and 100, and the player keeps guessing until they find it.

### Instructions

1. Define a function named `game_on`.
2. Inside the function, pick a random integer between 1 and 100 using the `random` module.
3. Keep asking the player for a guess until the guess is correct.
4. If the player enters anything except an integer, print `Wrong input type. Enter an integer number.` and ask again. This does not count as an attempt.
5. If the guess is below 1 or above 100, print `Out of range.` and ask again. This does not count as an attempt.
6. For every valid guess, add 1 to the attempt count.
7. If the guess is too high, print `The number is less than {guess}`. If the guess is too low, print `The number is greater than {guess}`.
8. When the player guesses correctly, return this message: `You have guessed the number {number} correctly in {attempts} attempts.`
9. Call the function and print the result.

### Example

For this example, assume the randomly generated secret number is 42.

```
Guess the integer number between 1 and 100: 50
The number is less than 50
Guess the integer number between 1 and 100: abc
Wrong input type. Enter an integer number.
Guess the integer number between 1 and 100: 150
Out of range.
Guess the integer number between 1 and 100: 30
The number is greater than 30
Guess the integer number between 1 and 100: 42
You have guessed the number 42 correctly in 3 attempts.
```

Only 50, 30 and 42 are counted as attempts. `abc` and `150` are invalid, so they are skipped.
