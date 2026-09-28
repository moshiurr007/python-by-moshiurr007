## Strong Password Generator

### Challenge

Create a strong password generator that creates a password from the user's desired password length. Use Python's built-in `secrets` and `string` modules only.

### Instructions

1. Import the `secrets` and `string` modules.
2. Create a function called `generate_password()` that takes no arguments.
3. Create separate strings containing lowercase letters, uppercase letters, numbers, and special characters. Then combine them into one string `all_characters`.
4. Ask the user to enter the password length and convert it to an integer.
5. Validate that the password length is between `8` and `30`. Otherwise, raise a `ValueError` with a helpful message.
6. Create a list called `password` containing at least one randomly selected character from each category: lowercase letters, uppercase letters, numbers, and special characters.
7. Use a loop to fill the remaining positions in the `password` with random characters from `all_characters`.
8. Securely shuffle the password characters.
9. Return the completed password as a string.

### Example

Input:<br>

`print(generate_password())`

Output:

```
Enter password length: 16
zsN):P^qH<RVp1jI
```
